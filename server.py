import socket

def udp_server(host='0.0.0.0', port=9750):
    """
    A UDP server that listens for messages on a specific port.

    :param host: The IP address to bind to (default: '0.0.0.0', meaning all available interfaces).
    :param port: The port number to listen on.
    """
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified host and port
    server_address = (host, port)
    print(f"Starting UDP server on {host}:{port}")
    udp_socket.bind(server_address)

    try:
        while True:
            # Wait for a message (buffer size is 1024 bytes)
            print("Waiting for a message...")
            data, client_address = udp_socket.recvfrom(1024)

            # Print the received message and client info
            print(f"Received message: {data.decode('utf-8')} from {client_address}")
            print(f"Received message: {data} from {client_address}")

    except KeyboardInterrupt:
        print("\nServer stopped by user.")

    finally:
        udp_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    udp_server()
