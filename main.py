"""
NC STATE CSE 573 PROJECT 2

@author kylebeard, hongyifan

------------------------------
The P2MP-FTP client will play the role of the sender that connects to a set of P2MP-FTP servers that play
the role of the receivers in the reliable data transfer. All data transfers are from sender (client) to
receivers (servers) only; only ACK packets travel from receivers to sender.

"""

import sys
import client
import server

if __name__ == "__main__":

    # Invoke server: p2mpserver port# file-name p
    # --> ex: python main.py p2mpserver 7735 test.txt 0.1

    # Invoke client: p2mpclient server-1 server-2 server-3 server-port# file-name MSS
    # --> ex: python main.py p2mpclient server1 server2 server3 7735 test.txt 500

    # handle actions for client or server based on command argument
    if sys.argv[1] == "p2mpserver":

        # extract parameters from command line argument
        port = sys.argv[2]
        filename = sys.argv[3]
        lossProbability = sys.argv[4]

        # initialize Receiver class to setup listener on port
        ftp = server.FTPReceiver()
        ftp.listen(port, filename)

    elif sys.argv[1] == "p2mpclient":

        # extract parameters from command line argument
        port = sys.argv[len(sys.argv) - 3]
        filename = sys.argv[len(sys.argv) - 2]
        mss = sys.argv[len(sys.argv) - 1]

        # initialize Sender class to setup each client to connect to port
        ftp = client.FTPSender()
        for i in range(2, len(sys.argv) - 3, 1):
            ftp.startClient(sys.argv[i], port, filename, mss)

    else:
        print("Command not recognized. Please enter p2mpserver or p2mpclient with arguments")
