import sys, socket, re, selectors

#Setting up the socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Variables we will be using in the client/server connection
hostorip = ''
port = 0   #initializing to number (changed later)
fileName = ''

#We now insert the command line arguments in their proper variable
if len(sys.argv) < 4:   # for the program name, host, port, and file name
    print('You are missing a command line argument. You need the host name or IP, port number, and the name of the file you will transfer.')
    sys.exit(1)
else:
    if 1 <= sys.argv[2] <= 65535:
        port = sys.argv[2]
    else:
        print("The port number is NOT valid.")
        sys.exit(1)
    hostorip, fileName = sys.argv[1], sys.argv[3]


sock.connect((hostorip,port)) #connects remote ip address and port

#Sends buffer
length = sock.send(b"accio\r\n")
print("Send bytes", length)



b = sock.recv(209715200)
print("Received: '%s'", b)



clientSocket.close()
sock.close()

sys.exit(0)