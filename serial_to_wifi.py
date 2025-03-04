import time
import serial
import random

SERIAL_PORT = "COM25"
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT}")

    responses = [
        "Ready and standing by.\r\r\n",
        "Drone armed.\r\r\n",
        "Takeoff complete.\r\n",
        "Formation aligned.\r\n",
        "LED sequence running.\r\n",
        "Executing routine.\r\n",
        "Formation changed.\r\n",
        "Brightness adjusted.\r\n",
        "Finale ready.\r\n",
        "Landing now.\r\n",
        "Landed and LEDs off.\r\n"
    ]

    print("Press Ctrl+C to stop.")

    while True:
        response = random.choice(responses)  # Pick a random response
        ser.write(response.encode())  # Send response over serial
        print(f"Sent: {response.strip()}")

        time.sleep(1)  # Wait before sending the next response

except serial.SerialException as e:
    print(f"Serial error: {e}")
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial connection closed.")
