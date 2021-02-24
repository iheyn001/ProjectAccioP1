import sys, getopt, socket

sock = socket.socket(family=AF_INET,type=SOCKET_STREAM)

hostorip = ''
port = 0   #initializing to number (changed later)
fileName = ''

#Goal: $ python3 client.py <HOSTNAME-OR-IP> <PORT> <FILENAME>

try:   #gets command line input
    opts, args = getopt.getopt(argv, "sh:p:i:", ["hostip=","portnum=","ifile="])
except getopt.GetoptError:   #in case there was a problem with the input
    print 'python3 client.py -h <HostorIP> -p <portNum> -f <fileName>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-s'   #ideally this would cover "python3 client.py"
        print 'python3 client.py -h <HostorIP> -p <portNum> -f <fileName>'
        sys.exit()
    elif opt in ("-h","--hostip"):
        hostorip = arg
    elif opt in ("-p", "--portnum"):
        port = arg
    elif opt in ("-p", "--ifile"):
        fileName = arg

sock.bind(hostorip, port)

sock.listen(1)
clientSocket, clientAddress = sock.accept()






    #elif hostname and port number incorrect
    #elif hostname incorrect
    #elif portname incorrect
    #elif fileName doesn't exist
    #else
        #if file is larger than 250 MiB
        #Invalid, terminate

#client must be able to specified server and port
#should NOT send anything until full accio\r\n comman is received
#Graceful processing of incorrect hostname and port number with a non-zero exit code
#print out standard error using sys.stderr.write() + an error message that starts with ERROR str
#Client application should exit with code zero after successful transfer of the file to server.
#It should support transfer of reasonably large files (100 MiB or more).
#Client should handle connection and transmission errors.
# The reaction to network or server errors should be no longer that 10 seconds

#wait 10 seconds