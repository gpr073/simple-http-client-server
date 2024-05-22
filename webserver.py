import socket

HOST = '127.0.0.1'
PORT = 50007

try:
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Prevents from getting Address alredy in use error
            s.bind((HOST, PORT)) # Binds the socket to host and port
            s.listen(0) # Listen for incoming connections
            print(f'Server listening on {HOST}:{PORT}')
            conn, addr = s.accept() # Accepts a connection
            with conn:
                print('Connected by', addr)
                data_buffer = b'' # Buffer to hold the data received
                while True:
                    data = conn.recv(4096) # Received upto 4096 bytes at a time
                    if not data:
                        break
                    data_buffer += data
                    if b"\r\n\r\n" in data_buffer:
                        break
                print("Full message recieved: ")
                print(data_buffer.decode()) # Decode the recieved bytes and print it
                conn.sendall(data_buffer) # Sned the received bytes back to client as response
except KeyboardInterrupt:
    print("\nServer is shutting down") # When a Keyboard Interrupt occurs, print this message
finally:
    s.close() # Close the socket