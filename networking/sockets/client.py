# Creating a client-side script to interact with the server using Python and sockets

# Import socket library for Python
import socket
# Host & port number
HOST = "127.0.0.1" # Localhost
PORT = 8000 # Server port which the client is going to connect to
# Create a new socket object with the family of IPv4 & TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the host and port number to the socket to connect to the server
    s.connect((HOST, PORT))
    # Send message to the server in a binary format
    s.sendall(b"Hello from the client")
    # Receive back the response from the server
    data = s.recv(1024) 
   # Print received data to the console
print(data)
