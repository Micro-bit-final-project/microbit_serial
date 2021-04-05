import serial
import serial.tools.list_ports as list_ports

# microbit's product and vendor IDs
PID = 516
VID = 3368

def connect():
    """
    Retrieve and return microbit's serial port.
    Returns false if no microbit is found.
    Heavily based on https://stackoverflow.com/questions/58043143/how-to-set-up-serial-communication-with-microbit-using-pyserial
    """
    microbit_port = serial.Serial(baudrate=115200, timeout=0.1) # microbit's baudrate
    ports = list(list_ports.comports())
    for p in ports:
        try:
            if p.pid == PID and p.vid == VID:
                microbit_port.port = str(p.device)
                return microbit_port # return microbit port
        except AttributeError:
            continue

    return False # No microbit found


def data(port):
    """
    This function reads the message coming in through serial from the microbit.
    port - a serial.Serial object rappresenting the port used for the 
           connection with the microbit.
    """
    try:
        message = port.readline().decode("utf-8")
    except Exception:
        return [-1, -1, -1, -1]
    if message:
        try:
            message = message.replace('\r', '')  # Remove carriage return
            message = message.replace('\n', '')  # Remove line feed
            message = message[1:-1]  # Remove array parenthesis []

            # Convert string message to float array
            message = message.split(",")
            data = []
            for item in message:
                data.append(float(item))
            return data
        except UnicodeDecodeError:
            print("Invalid message")
            return [0, 0, 0, 0]
        except ValueError:
            print("Invalid message")
            return [0, 0, 0, 0]
    return False