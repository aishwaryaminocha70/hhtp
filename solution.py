# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(('127.0.0.1', 13331))
  #Fill in start
  serverSocket.listen(1)
  #Fill in end
  

  while True:
    #print('Ready to serve..')
    #Establish the connection
    
    connectionSocket, addr = serverSocket.accept(.encode())
  
    try:
      
      try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:].decode())
        outputdata = f.read(.decode())     
        


        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())                              
        connectionSocket.close()
      except IOError:
        
        # Send response message for file not found (404)
      
        connectionSocket.send(\nHTTP/1.1 404 Not Found\n\n')
        
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass
      serverSocket.close()
      sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
  
