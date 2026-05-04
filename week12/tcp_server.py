#!/usr/bin/env python3
"""
Simple TCP server: accept one client, print message, send reply.

Usage:
1. Run server first: python3 tcp_server.py
2. In another terminal run: python3 tcp_client.py
"""

import socket

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024


# Create and configure a TCP server socket.
def create_server_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    return server_socket


# Receive one text message from client.
def receive_client_message(connection):
    data = connection.recv(BUFFER_SIZE)
    return data.decode("utf-8")


# Send one text reply to client.
def send_client_reply(connection, message):
    connection.sendall(message.encode("utf-8"))


# Handle one client connection.
def handle_client(connection, address):
    print(f"Connected by {address}")
    message = receive_client_message(connection)
    print(f"Received from client: {message}")
    reply = "Hello, Client! I received your message."
    send_client_reply(connection, reply)


# Run the server workflow.
def main():
    server_socket = create_server_socket(HOST, PORT)
    print(f"TCP server listening on {HOST}:{PORT}")

    connection, address = server_socket.accept()
    with connection:
        handle_client(connection, address)

    server_socket.close()


if __name__ == "__main__":
    main()
