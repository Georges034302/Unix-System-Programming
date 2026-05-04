#!/usr/bin/env python3
"""
Simple TCP client: connect to server, send message, print reply.

Usage:
1. Start server first: python3 tcp_server.py
2. Then run client: python3 tcp_client.py
"""

import socket

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024


# Create and connect a TCP client socket.
def create_client_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket


# Send one text message to server.
def send_server_message(client_socket, message):
    client_socket.sendall(message.encode("utf-8"))


# Receive one text reply from server.
def receive_server_reply(client_socket):
    data = client_socket.recv(BUFFER_SIZE)
    return data.decode("utf-8")


# Run the client workflow.
def main():
    client_socket = create_client_socket(HOST, PORT)

    message = "Hello, Server!"
    send_server_message(client_socket, message)

    response = receive_server_reply(client_socket)
    print(f"Received from server: {response}")

    client_socket.close()


if __name__ == "__main__":
    main()
