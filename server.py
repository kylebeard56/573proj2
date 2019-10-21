"""
NC STATE CSE 573 PROJECT 2

@author kylebeard, hongyifan

------------------------------
The server listens on the well-known port 7735. It implements the receiver side of the Stop-and-Wait protocol,
as described in the book. Specifically, when it receives a data packet, it computes the checksum and checks
whether it is in-sequence, and if so, it sends an ACK segment (using UDP) to the client; it then writes
the received data into a file whose name is provided in the command line. If the packet received is out-ofsequence,
an ACK for the last received in-sequence packet is sent;, if the checksum is incorrect, the receiver does nothing.

"""

import sys
import socket


# The P2MP-FTP Server (Receiver) --> Kyle Beard to implement
class FTPReceiver:

    def __init__(self):
        pass

    def listen(self, port):

        # NOTE: https://pymotw.com/2/socket/tcp.html

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 10000)

        # Bind the socket to the port
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(port)

        # Wait for a connection
        while True:
            print >> sys.stderr, 'Waiting for a connection...'
            connection, client_address = sock.accept()
            self.connected(connection, client_address)

    # This function computes the checksum from the received data to validate
    def validateChecksum(self, data):

        # todo: write checksum validation algorithm
        return True

    # This function is called when the server listening is connected with a client
    def connected(self, connection, client):

        # Handle the connection
        try:
            print >> sys.stderr, 'Connection from ', client

            message = ""
            sequence = 0

            # Receive the data in small chunks and retransmit it
            while True:

                # Receive message and append to full message
                data = connection.recv(16)
                message += data
                print >> sys.stderr, 'received "%s"' % data

                # todo: check data and compute checksum here
                isChecksumCorrect = self.validateChecksum(data)

                # check if the checksum is incorrect, the receiver does nothing
                if ~isChecksumCorrect:
                    print("checksum incorrect")
                    break

                # check if data returned in-sequence, otherwise don't increment
                # todo: verify this is how in-sequence or out-of-sequence will be handled
                if self.getSequence(data) == sequence:
                    print("in-sequence data received")
                    sequence += 1
                else:
                    print("out-of-sequence data received - resending ack")

                # Construct ACK here tuple and increment sequence number
                ack = (sequence, 0000000000000000, 1010101010101010)

                if data:
                    print >> sys.stderr, 'Sending ACK back to the client '
                    connection.sendall(ack)
                else:
                    print >> sys.stderr, 'No more data from ', client
                    break

        finally:
            # Clean up the connection
            connection.close()