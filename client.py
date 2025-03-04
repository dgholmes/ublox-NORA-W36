# import socket
# import time
#
#
# def udp_client(host='10.42.0.60', port=9750, message="Hello, F40 ready to dazzle the crowd?", interval=1):
#     """
#     Continuously send a UDP message to a specified server.
#
#     :param host: The server IP address.
#     :param port: The server port number.
#     :param message: The string message to send.
#     :param interval: Time delay (seconds) between consecutive messages.
#     """
#     # Create the UDP socket
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     server_address = (host, port)
#
#     print(f"Sending messages to {host}:{port}. Press Ctrl+C to stop.")
#     try:
#         while True:
#             # Send the message
#             udp_socket.sendto(message.encode(), server_address)
#             print(f"Sent: {message}")
#
#             # Wait for the specified interval
#             time.sleep(interval)
#
#     except KeyboardInterrupt:
#         print("\nStopped by user.")
#
#     finally:
#         udp_socket.close()
#         print("Socket closed.")
#
#
# if __name__ == "__main__":
#     # You can modify host, port, message, and interval here
#     udp_client(host='10.42.0.60', port=9750, message="Hello, F40 ready to dazzle the crowd?\n", interval=1)

import socket
import time
import random


def udp_client(host='10.42.0.60', port=9750, interval=1):
    """
    Continuously send random UDP messages to a drone from the control station.

    :param host: The drone's IP address.
    :param port: The drone's port number.
    :param interval: Time delay (seconds) between consecutive messages.
    """
    messages = [
        "Hello, F40 ready to dazzle the crowd.\n",
        "Arm the drone and prepare for the light show.\n",
        "Takeoff and reach initial hover position.\n",
        "Align with formation grid.\n",
        "Start synchronized LED pattern sequence.\n",
        "Execute aerial choreography routine.\n",
        "Transition to next formation.\n",
        "Adjust brightness and color for effect.\n",
        "Prepare for finale sequence.\n",
        "Descend gradually for landing.\n",
        "Shutdown LEDs and complete landing sequence.\n"
    ]

    # Create the UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)

    print(f"Sending commands to drone at {host}:{port}. Press Ctrl+C to stop.")
    try:
        while True:
            message = random.choice(messages)
            udp_socket.sendto(message.encode(), server_address)
            print(f"Sent: {message}")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        udp_socket.close()
        print("Socket closed.")


if __name__ == "__main__":
    udp_client(host='10.42.0.60', port=9750, interval=1)
