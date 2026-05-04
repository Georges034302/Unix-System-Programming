#!/usr/bin/env python3
"""
Simple UDP server: receive one datagram, print it, send reply.

Usage:
1. Run server first: python3 udp_server.py
2. In another terminal run: python3 udp_client.py
"""

import socket

HOST = "127.0.0.1"
PORT = 65433
BUFFER_SIZE = 1024


# Create and bind a UDP server socket.
def create_udp_server_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    return server_socket


# Receive one UDP message and sender address.
def receive_udp_message(server_socket):
    data, address = server_socket.recvfrom(BUFFER_SIZE)
    return data.decode("utf-8"), address


# Send one UDP reply back to sender.
def send_udp_reply(server_socket, address, message):
    server_socket.sendto(message.encode("utf-8"), address)


# Run the UDP server workflow.
def main():
    server_socket = create_udp_server_socket(HOST, PORT)
    print(f"UDP server listening on {HOST}:{PORT}")

    message, address = receive_udp_message(server_socket)
    print(f"Received from {address}: {message}")

    reply = "Hello, Client! I received your UDP message."
    send_udp_reply(server_socket, address, reply)

    server_socket.close()


if __name__ == "__main__":
    main()
