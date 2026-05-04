#!/usr/bin/env python3
"""
Simple UDP client: send one datagram to server and print reply.

Usage:
1. Start server first: python3 udp_server.py
2. Then run client: python3 udp_client.py
"""

import socket

HOST = "127.0.0.1"
PORT = 65433
BUFFER_SIZE = 1024


# Create a UDP client socket.
def create_udp_client_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Send one UDP message to server.
def send_udp_message(client_socket, host, port, message):
    client_socket.sendto(message.encode("utf-8"), (host, port))


# Receive one UDP reply from server.
def receive_udp_reply(client_socket):
    data, _address = client_socket.recvfrom(BUFFER_SIZE)
    return data.decode("utf-8")


# Run the UDP client workflow.
def main():
    client_socket = create_udp_client_socket()

    message = "Hello, UDP Server!"
    send_udp_message(client_socket, HOST, PORT, message)

    response = receive_udp_reply(client_socket)
    print(f"Received from server: {response}")

    client_socket.close()


if __name__ == "__main__":
    main()
