import serial
import time

SERIAL_PORT = "COM3"
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT}")

    # commands = ["AT", "AT+GMI", "AT+GMM", "AT+GMR", "AT+GSN", "AT+UWHN=swarm"]
    commands = ["AT+USYDS", "AT&W", "AT+CPWROFF"] # this is for reseting to default settings

    # commands = ["AT+UWSNST=0", "AT+UWSNST=1", "AT+UWSNST=2"] # this is for viewing saved net_ip settings
    # commands = ["AT+UWSIPS=0,192.168.0.50,255.255.0.0,192.168.0.1", "AT&W", "AT+UWSIP=0"] # setting static ip
    # commands = ["AT+UWSCP=0,PABLO_DMD", "AT+UWSSW=0,Pablo180808!@,0", "AT&W","AT+UWSC=0", "AT+UWSNST=0", "AT+UWSST=4"]
    # commands = ["AT+UWSDC"] #disable connection

    # Set static IP
    commands = ["AT+UWSIPS=0,10.42.0.60,255.255.255.0,10.42.0.1", "AT&W", "AT+UWSIP=0"] # 1. setting static ip
    commands = ["AT+UWSCP=0,\"swarm\"", "AT+UWSSO=0", "AT&W","AT+UWSC=0", "AT+UWSNST=0", "AT+UWSST=4"] # 2. Set Wi-Fi connection settings
    #
    # Wi-Fi UDP Client: create socket, connect and send string
    commands = ["AT+USOCR=17", "AT+USOC=0,\"10.42.0.4\",9750", "AT&W"] # create socket -> connect socket (client)
    # Wi-Fi UDP Client (Listener): create listener socket, connect and read string
    commands = ["AT+USOCR=17", "AT+USOL=1,9750", "AT&W"]  # (temporary) create socket -> connect socket (server-listener)

    commands = ["AT+USOPCR=17,0", "AT+USOP=100,\"10.42.0.4\",9750", "AT&W", "AT+CPWROFF"] # create persistent socket
    # commands = ["AT+USOPCR=17,0", "AT+USOP=100,9750", "AT&W", "AT+CPWROFF"]  # create persistent socket

    # commands = ["AT+USOWS=100,\"Hello from NORA-W36\""] # socket write string
    # commands = ["AT+USORS=0,19"] # Read socket string
    commands = ["AT+USOWS=100,\"Hello from NORA-W36\"","AT+USORS=1,19"]

    # commands = ["AT+USOCL=100"] # Remove socket
    # commands = ["AT+USOPR=100"]  # Remove socket
    # commands = ["AT+UTMP=1,0"] # Enable Persistant on the connection
    # commands = ["AT+USOPL?"] # Socket Persistent List

    for command in commands:
        ser.write((command + "\r\n").encode())  # Send command
        time.sleep(1)  # Wait for response
        raw_response = ser.read(ser.in_waiting)  # Read raw data (up to 100 bytes)
        print(f"Command: {command} -> Raw Response: {raw_response}")

except serial.SerialException as e:
    print(f"Serial error: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
