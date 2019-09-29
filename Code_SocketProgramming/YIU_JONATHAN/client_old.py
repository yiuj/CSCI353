import socket               # Import socket module
import sys

if (len(sys.argv) != 9 or sys.argv[1] != '-s' or sys.argv[3] != '-p' or sys.argv[5] != '-l' or sys.argv[7] != '-n'):
    print('Usage Instructions: client.py –s <serverIP> –p <portno> –l <logfile> –n <myname>')
else:
    serverIP = sys.argv[2]
    portno = sys.argv[4]
    logfilename = sys.argv[6]
    clientName = sys.argv[8]

    logFile = open(logfilename, "a")

    def log(string):
        logFile.write(string + "\n")

    def getSocket():
        s = socket.socket()                     # Create a socket object
        # port = 12345
        s.connect(('localhost', int(portno)))          # Establish connection/handshake
        return s


    sock = getSocket()
    log("connecting to server localhost at port " + portno)
    try:
        registerMessage = "register " + clientName
        sock.send(registerMessage.encode())
        log("sending register message " + clientName)
        welcomeMessage = sock.recv(1024).decode()
        if welcomeMessage == "welcome " + clientName:
            log ("received welcome")
            inputString = True
            while(inputString):
                user_input=str(input('> '))
                if user_input != 'exit':
                    sock.send(user_input.encode())
                else:
                    inputString = False
                    log("terminating client...")
    except Exception as e:
        print (e)
    finally:
        sock.close()





