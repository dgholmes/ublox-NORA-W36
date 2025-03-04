import socket
import time
from pymavlink import mavutil
import random

# Connect to the MAVLink instance (this is a common setup)
master = mavutil.mavlink_connection('udpout:10.42.0.60:9750')


def udp_client(host='10.42.0.60', port=9750, interval=1):
    """
    Send drone control commands using MAVLink over UDP based on user input or send random messages.

    :param host: The drone's IP address.
    :param port: The drone's port number.
    :param interval: Time delay (seconds) between consecutive messages.
    """
    # Create the UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)

    # Messages for random sending
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

    print(f"Sending commands to drone at {host}:{port}. Type a number (1-6) and press Enter to send the command.")
    print("Available commands:")
    print("1: Arm Drone")
    print("2: Disarm Drone")
    print("3: Takeoff")
    print("4: Land")
    print("5: Motor Test")
    print("6: Send Random Message")

    try:
        while True:
            # Get user input to select a command
            command = input("Enter the command number: ")

            if command == "1":
                arm_drone()
            elif command == "2":
                disarm_drone()
            elif command == "3":
                take_off()
            elif command == "4":
                land()
            elif command == "5":
                motor_test(1)  # Example motor number, adjust as necessary
            elif command == "6":
                send_random_message(udp_socket, server_address, messages)
            else:
                print("Invalid command. Please enter a number between 1 and 6.")

            # Wait a little before asking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        udp_socket.close()
        print("Socket closed.")


def send_random_message(udp_socket, server_address, messages):
    """Send a random message from the predefined list."""
    message = random.choice(messages)
    udp_socket.sendto(message.encode(), server_address)
    print(f"Sent: {message}")


def arm_drone():
    global ack_msg
    try:
        master.mav.command_long_send(master.target_system, master.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack_msg:
            if ack_msg.result == 0:
                print("Armed successfully!")
            else:
                print(f"Arming failed: {ack_msg.result}")
    except Exception as e:
        print(f"Error sending arm command: {e}")
    finally:
        print(ack_msg)


def disarm_drone():
    global ack_msg
    try:
        master.mav.command_long_send(master.target_system, master.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 0, 0, 0, 0, 0, 0)
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack_msg:
            if ack_msg.result == 0:
                print("Disarmed successfully!")
            else:
                print(f"Disarming failed: {ack_msg.result}")
    except Exception as e:
        print(f"Error sending disarm command: {e}")
    finally:
        print(ack_msg)


def take_off(take_off_alt=2.5):
    try:
        master.mav.command_long_send(master.target_system, master.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, take_off_alt)
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack_msg:
            if ack_msg.result == 0:
                print(f"Take off to altitude {take_off_alt}m successful!")
            else:
                print(f"Take off failed: {ack_msg.result}")
    except Exception as e:
        print(f"Error sending take off command: {e}")


def land():
    try:
        master.mav.command_long_send(master.target_system, master.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0)
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack_msg:
            if ack_msg.result == 0:
                print("Landing successful!")
            else:
                print(f"Landing failed: {ack_msg.result}")
    except Exception as e:
        print(f"Error sending land command: {e}")


def motor_test(motor):
    try:
        master.mav.command_long_send(master.target_system, master.target_component,
                                     mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST, 0, motor, 0, 20, 2, 0, 0, 0)
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        if ack_msg:
            if ack_msg.result == 0:
                print("Test successful!")
                print(ack_msg)
            else:
                print(f"Test failed: {ack_msg.result}")
    except Exception as e:
        print(f"Error sending motor test command: {e}")


if __name__ == "__main__":
    udp_client(host='10.42.0.60', port=9750)
