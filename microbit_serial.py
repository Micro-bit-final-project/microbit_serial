import serial
import serial.tools.list_ports as list_ports

# microbit's product and vendor IDs
PID = 516
VID = 3368

def connect():
    """
    Retrieve and return microbit's serial port.
    Returns false if no microbit is found.
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