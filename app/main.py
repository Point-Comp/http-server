import socket  # noqa: F401


def main():
    print("Server starting on localhost:4221...")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()  # Wait for one client

    # Read the request (first 1024 bytes)
    request = conn.recv(1024).decode("utf-8")
    # Extract the path from the request line
    path = request.split(" ")[1]  # second word is the path

    # Send the correct response
    if path == "/":
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

    conn.close()

if __name__ == "__main__":
    main()
