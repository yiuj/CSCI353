
import socket               								# Import socket module
import sys

if (len(sys.argv) != 5 or sys.argv[1] != '-p' or sys.argv[3] != '-l'):
    print('Usage Instructions: server –p <portno> –l <logfile>')
else:
    portno = sys.argv[2]
    logfileName = sys.argv[4]

    logFile = open(logfileName, "a")

    def log(string):
        print(string)
        logFile.write(string + "\n")

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        # Create a socket object
    # port = 12345                								# Reserve a port for your service.
    s.bind(('localhost', int(portno)))        							# Bind to the port
    log("server started on localhost at port " + portno + "... ")

    try:
        while True:
            data, client_address = s.recvfrom(1024)
            message = str(data.decode())
            # log("client connection from host port")
            if (data):
                print (" Data received from client : ", message)
                if message.split() and message.split()[0] == "register":
                    log("client connection from host port")
                    log("received " + message + " from host port")
                    welcomeMessage = "welcome " + message.split()[1]
                    s.sendto(welcomeMessage.encode(), client_address)
    except Exception as e:
        print(e)
    finally:
        log("terminating server...")
