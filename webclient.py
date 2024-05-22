import socket
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) < 2:
    print("Usage: python webclient.py <hostname> [port]")
    sys.exit(1)

# Get the hostname and port from the cli arguments
HOST = sys.argv[1]
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 80
print("Inputs ", HOST, PORT)

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) # Connects the socket to the server
    request = f"GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode()) # Sends the request to the server
    response = b'' # Buffer to store the received data
    while True:
        data = s.recv(4096) # Receiving data from the server 4096 bytes at a time
        if not data: # Loop runs till all the data has been recieved
            break
        response += data

response_str = response.decode() # Decoding bytes to string
print("Raw data:\n", response)
print('Response string:\n', response_str)

# headers, _, body = response_str.partition('\r\n\r\n')
# print('Headers:\n', headers)
# print('Body', body)