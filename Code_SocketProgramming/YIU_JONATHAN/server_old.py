
import socket               # Import socket module
import time
import sys

if (len(sys.argv) != 5 or sys.argv[1] != '-p' or sys.argv[3] != '-l'):
    print('Usage Instructions: server –p <portno> –l <logfile>')
else:
    portno = sys.argv[2]
    logfilename = sys.argv[4]

    logFile = open(logfilename, "a")

    def log(string):
        logFile.write(string + "\n")

    s = socket.socket()         # Create a socket object
    # port = 12345                # Reserve a port for your service.
    s.bind(('localhost', int(portno)))        # Bind to the port
    log("server started on localhost at port " + portno + "... ")

    s.listen(5)                 # Now wait for client connection.

    try:
        connection, client_address = s.accept()     # Establish connection with client.
        if connection:
            log("client connection from host port")
            while True:
                data = connection.recv(1024)
                message = str(data.decode())
                if message.split() and message.split()[0]:
                    log("received " + message + " from host port")
                    welcomeMessage = "welcome " + message.split()[1]
                    connection.send(welcomeMessage.encode())
    except Exception as e:
        print (e)
    finally:
        log("terminating server...")