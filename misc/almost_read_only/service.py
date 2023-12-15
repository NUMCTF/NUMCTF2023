import socket
import subprocess

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one incoming connection

    print(f"Listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        while True:
            client_socket.send("\n$ ".encode())

            command = client_socket.recv(1024).decode('utf-8')
            print(f"Received command: {command}")

            if not command:
                break  # Break the loop if the command is empty (client closed the connection)
            command = command[:2]
            try:
                result = subprocess.check_output(command, shell=True)
                client_socket.send(result)
            except Exception as e:
                client_socket.send(str(e).encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Use 0.0.0.0 to listen on all available interfaces
    PORT = 10004

    start_server(HOST, PORT)
