import socket               # Import socket module
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 9 or sys.argv[1] != '-s' or sys.argv[3] != '-p' or sys.argv[5] != '-l' or sys.argv[7] != '-n'):
        print('Usage Instructions: client.py –s <serverIP> –p <portno> –l <logfile> –n <myname>')
    else:
        serverIP = sys.argv[2]
        portno = sys.argv[4]
        logfilename = sys.argv[6]
        clientName = sys.argv[8]

        logFile = open(logfilename, "a")

        def log(string):
            print(string)
            logFile.write(string + "\n")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', int(portno))
        log("connecting to server localhost at port " + portno)

        try:
            # send register message
            registerMessage = "register " + clientName
            sock.sendto(registerMessage.encode(), server_address)
            log("sending register message " + clientName)

            # receive welcome message
            data, server_detail = sock.recvfrom(1024)
            welcomeMessage = data.decode()
            if welcomeMessage == "welcome " + clientName:
                log("received welcome")
                # start listening for server response
                inputAvailable = True
                while(inputAvailable):
                    user_input=str(input('> '))
                    if user_input != 'exit':
                        sock.sendto(user_input.encode(), server_address)
                    else:
                        inputAvailable = False
                        log("terminating client...")
        except Exception as e:
            print (e)
        finally:
            sock.close()





