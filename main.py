"""
NC STATE CSE 573 PROJECT 2

@author kylebeard, hongyifan
"""

import sys

"""
The P2MP-FTP client will play the role of the sender that
connects to a set of P2MP-FTP servers that play the role of the receivers in the reliable data transfer.
All data transfers are from sender (client) to receivers (servers) only; only ACK packets travel from receivers
to sender.
"""

# The P2MP-FTP Server (Receiver)
class FTPServer:

    def main(self):
        print("FTPServer class setup")

    def connectServer(self):
        print("connect")

# The P2MP-FTP Client (Sender)
class FTPClient:

    def main(self):
        print("FTPClient class setup")

    def connectClient(self, name, port, mss):
        print("Connecting client: " + str(name))


if __name__ == "__main__":

    # Invoke server: p2mpserver port# file-name p
    # --> ex: python main.py p2mpserver 7735 test.txt 0.1

    # Invoke client: p2mpclient server-1 server-2 server-3 server-port# file-name MSS
    # --> ex: python main.py p2mpclient server1 server2 server3 7735 test.txt 500

    argLength = len(sys.argv)
    invokation = sys.argv[1] # either p2mpserver or p2mpclient
    print(invokation)

    # handle actions for client or server based on command argument
    if invokation == "p2mpserver":
        print("do stuff")
    elif invokation == "p2mpclient":

        # extract parameters from command line argument
        port = sys.argv[argLength - 3]
        filename = sys.argv[argLength - 2]
        mss = sys.argv[argLength - 1]
        print(str(port) + " " + str(filename) + " " + str(mss))

        # get name and connect each client to the server
        ftp = FTPClient()
        for i in range(2, argLength - 3, 1):
            ftp.connectClient(sys.argv[i], port, mss)

    else:
        print("Command not recognized. Please enter p2mpserver or p2mpclient with arguments")
