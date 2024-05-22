import socket

HOST = 'google.com'
PORT = 80

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
print('Response string:\n', response_str)

# headers, _, body = response_str.partition('\r\n\r\n')
# print('Headers:\n', headers)
# print('Body', body)