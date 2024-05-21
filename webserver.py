import socket

HOST = '127.0.0.1'
PORT = 50007

try:
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(0)
            print(f'Server listening on {HOST}:{PORT}')
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data_buffer = b''
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    data_buffer += data
                    if b"\r\n\r\n" in data_buffer:
                        break
                print("Full message recieved: ")
                print(data_buffer.decode())
                conn.sendall(data_buffer)
except KeyboardInterrupt:
    print("\nServer is shutting down")
finally:
    s.close()