
import socket               								# Import socket module
import sys

if (len(sys.argv) != 5 or sys.argv[1] != '-p' or sys.argv[3] != '-l'):
    print('Usage Instructions: server –p <portno> –l <logfile>')
else:
    portno = sys.argv[2]
    logfileName = sys.argv[4]

    # map of name to address
    nameToAddressMap = {}
    addressToNameMap = {}


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
                print (" **** Data received from client : ", message, "****")
                # if register message
                if message.split() and message.split()[0] == "register":
                    log("client connection from host port")
                    log("received " + message + " from host port")
                    nameToAddressMap[message.split()[1]] = client_address
                    addressToNameMap[client_address] = message.split()[1]
                    welcomeMessage = "welcome " + message.split()[1]
                    s.sendto(welcomeMessage.encode(), client_address)
                elif message.split() and message.split()[0] == "sendto":
                    receiver = message.split()[1]
                    sender = addressToNameMap[client_address]
                    log("sendto " + receiver +  " from " + sender + " " + message.split(" ", 2)[2])
                    messageToSend = "recvfrom " + sender + " to " + receiver + " " + message.split(" ", 2)[2]
                    s.sendto(messageToSend.encode(), nameToAddressMap[receiver])
                    log("recvfrom " + sender +  " from " + receiver + " " + message.split(" ", 2)[2])
    except Exception as e:
        print(e)
    finally:
        log("terminating server...")
