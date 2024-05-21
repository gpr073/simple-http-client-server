import socket

HOST = 'google.com'
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    request = f"GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())
    response = b''
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

response_str = response.decode()
print('Response string:\n', response_str)

# headers, _, body = response_str.partition('\r\n\r\n')
# print('Headers:\n', headers)
# print('Body', body)