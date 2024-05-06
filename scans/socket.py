import socket


async def perform_scan():
    # Create a socket and connect to a remote host
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('example.com', 80))
            return "Port 80 is open"
        except ConnectionRefusedError:
            return "Port 80 is closed"
