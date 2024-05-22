import socket

HOST = '127.0.0.1'
PORT = 50007

try:
    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Prevents from getting Address already in use error
        s.bind((HOST, PORT)) # Binds the socket to host and port
        s.listen() # Listen for incoming connections

    # Keep the server running forever until an interrupt or error occurs.
        while True:
            print(f'Server listening on {HOST}:{PORT}\n')
            conn, addr = s.accept() # Accepts a connection
            with conn:
                print(f'Connected by {addr}\n')
                data_buffer = b'' # Buffer to hold the data received
                while True:
                    data = conn.recv(4096) # Receives upto 4096 bytes at a time
                    if not data:
                        break
                    data_buffer += data
                    if b"\r\n\r\n" in data_buffer:
                        break
                print("Full message recieved: ")
                print(data_buffer.decode()) # Decode the recieved bytes and print it
                conn.sendall(data_buffer) # Send the received bytes back to client as response
except KeyboardInterrupt:
    print("\nServer is shutting down") # When a Keyboard Interrupt occurs, print this message
