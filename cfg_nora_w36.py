import serial
import time


def send_command(ser, command, wait_time=0.5):
    """
    Sends an AT command to the serial device and waits for a response.
    """
    ser.write((command + "\r\n").encode())
    print(f"Sent: {command}")
    if command == "AT+CPWROFF":
        time.sleep(3)  # Allow time for response
    else:
        time.sleep(wait_time)  # Allow time for response
    response = ser.read_all().decode(errors='ignore').strip()
    print(f"Response: {response}\n")
    return response


def reset_and_reboot(ser):
    commands = ["AT+USYDS", "AT&W", "AT+CPWROFF"]
    execute_commands(ser, commands)


def configure_network(ser):
    commands = [
        "AT+UWSIPS=0,10.42.0.60,255.255.255.0,10.42.0.1",
        "AT+UWSIP=0"
    ]
    execute_commands(ser, commands)


def configure_wifi(ser):
    commands = [
        "AT+UWSCP=0,\"swarm\"",
        "AT+UWSSO=0",
        "AT+UWSC=0"
    ]
    execute_commands(ser, commands)


def configure_sockets(ser):
    commands = [
        "AT+USOPCR=17",
        "AT+USOP=100,\"10.42.0.4\",9750",
        "AT+USOPCR=17",
        "AT+USOL=101,9750"
    ]
    execute_commands(ser, commands)


def save_and_reboot(ser):
    commands = ["AT&W", "AT+CPWROFF"]
    execute_commands(ser, commands)


def test_sockets(ser):
    commands = [
        "AT+USOWS=100,\"Hello from NORA-W36\"",
        "AT+USORS=101,1000",
        "AT+USORS=101,1000",
        "AT+USORS=101,1000"
    ]
    execute_commands(ser, commands)


def enter_transparent_mode(ser):
    commands = ["AT+UTMP=1,100", "AT+UTMP=1,101"]
    execute_commands(ser, commands)


def execute_commands(ser, commands):
    for cmd in commands:
        response = send_command(ser, cmd)
        if "ERROR" in response:
            print("Error detected, stopping execution.")
            break


def main():
    port = "COM25"  # Change to your actual port (e.g., "/dev/ttyUSB0" on Linux)
    baudrate = 115200  # Adjust based on device specifications

    try:
        ser = serial.Serial(port, baudrate, timeout=2)
        time.sleep(1)  # Allow time for connection initialization

        while True:
            print("\nSelect an option:")
            print("1. Reset and Reboot")
            print("2. Configure Network")
            print("3. Configure Wi-Fi")
            print("4. Configure Sockets")
            print("5. Save and Reboot")
            print("6. Test Sockets")
            print("7. Enter Transparent Mode")
            print("8. Run All")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                reset_and_reboot(ser)
            elif choice == "2":
                configure_network(ser)
            elif choice == "3":
                configure_wifi(ser)
            elif choice == "4":
                configure_sockets(ser)
            elif choice == "5":
                save_and_reboot(ser)
            elif choice == "6":
                test_sockets(ser)
            elif choice == "7":
                enter_transparent_mode(ser)
            elif choice == "8":
                reset_and_reboot(ser)
                configure_network(ser)
                configure_wifi(ser)
                configure_sockets(ser)
                save_and_reboot(ser)
                test_sockets(ser)
                enter_transparent_mode(ser)
                save_and_reboot(ser)
            elif choice == "9":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

        ser.close()
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()