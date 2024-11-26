# Creating a server-side script for working with sockets in Python

# Import socket library for Python
import socket
# Host & port number
HOST = "127.0.0.1"
PORT = 8000
# Create a new socket object with the family of IPv4 & TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the host and port to the socket as a tuple data structure
    s.bind((HOST, PORT))
    # Listen for incomming connections from the client side
    s.listen()
    # Accepting connection from the client and getting conn and addr objects as a tuple
    conn, addr = s.accept() # Creates a new socket object for accepting connections from the client and this is different from the original socket object above
    # Getting data from the client 
    with conn: # when using with clause we can at the end close the connection automatically without having to close it manually
        print(f"Connected by {addr}")
        while True:
            # Get data from the client while the connection is open
            data = conn.recv(1024)
            # If there's no data, break
            if not data:
                break
            # Send data back to the client
            conn.sendall(data)
            

