"""
NC STATE CSE 573 PROJECT 2

@author kylebeard, hongyifan

------------------------------
The P2MP-FTP client implements the sender in the reliable data transfer. When the client starts, it reads
data from a file specified in the command line, and calls rdt send() to transfer the data to the P2MP-FTP
servers. For this project, we will assume that rdt send() provides data from the file on a byte basis. The
client also implements the sending side of the reliable Stop-and-Wait protocol, receiving data from rdt send(),
buffering the data locally, and ensuring that the data is received correctly at the server.

The client also reads the value of the maximum segment size (MSS) from the command line. The Stop-andWait protocol
buffers the data it receives from rdt send() until it has at least one MSS worth of bytes. At
that time it forms a segment that includes a header and MSS bytes of data; as a result, all segments sent,
except possibly for the very last one, will have exactly MSS bytes of data.

The client transmits each segment separately to each of the receivers, and waits until it has received ACKs
from every receiver before it can transmit the next segment. Every time a segment is transmitted, the sender
sets a timeout counter. If the counter expires before ACKs from all receivers have been received, then the
sender re-transmits the segment, but only to those receivers from which it has not received an ACK yet. This
process repeats until all ACKs have been received (i.e., if there are n receivers, n ACKS, one from each
receiver have arrived at the sender), at which time the sender proceeds to transmit the next segment.

"""

import sys
import socket


# The P2MP-FTP Client (Sender) --> Hongyi Fan to implement
class FTPSender:

    def __init__(self):
        pass

    def startClient(self, name, port, filename, mss):

        # NOTE: https://docs.python.org/2/howto/sockets.html

        # create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect the client socket to the well-known server
        server_address = ('192.168.0.1', port)
        print("connecting client to server...")
        sock.connect(server_address)

        # listen for incoming connections
        sock.listen(5) # 5 is the number of connections requests

        # read file and call rdt_send
        print("reading file")
        f = open(filename + ".txt", "a")
        message = f.read()

        # call reliable data transfer 3.0 (stop-and-wait)
        self.rdt_send(sock, message, mss)

    def rdt_send(self, sock, message, mss):

        # todo: handle timeout and ack between this specific client (sender) and server (receiver)

        try:

            # transfer file
            print("sending " + message)
            sock.sendall(message)

            # look for the response
            amount_received = 0
            amount_expected = len(message)

            # todo: integrate timeout and ACK somehow in here
            # todo: include the random packet loss probability

            while amount_received < amount_expected:
                data = sock.recv(16) # todo: should this be MSS?
                amount_received += len(data)
                print("received " + data)

        finally:
            print("closing socket")
            sock.close()

