"""
Connectors
"""
import socket
import logging
import serial


LOG = logging.getLogger(__name__)

EOT = b"ok\r\n"


class Tcp2Serial:
    """ "
    tcp 2 serial adapter
    """

    def __init__(self, host, port, timeout=2):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = bytearray()
        self.sock.settimeout(timeout)

    def connect(self):
        self.sock.connect(self.host, self.port)

    def send(self, data):
        """
        send data over socket
        """
        self.sock.sendall(data)


    def read(self, n):
        """
        read n bytes from socket
        """
        while data[-4:] != EOT:
            packet = self.sock.recv(1)
            data.extend(packet)
        return data


class Serial:
    def __init__(self, port: str, speed: int):
        self.port = port
        self.speed = speed
        self.connector = None

    def connect(self):
        self.connector = serial.Serial(self.port, self.speed, timeout=1)


    def read(self, n):
        """
        read n bytes from serial port
        """
        while data[-4:] != EOT:
            packet = self.connector.read(1)
            data.extend(packet)
        return data

        ser = None
        try:
            ser = serial.Serial(port, speed, timeout=1)
            expected = "Grbl 1.1h ['$' for help]"
            result = ser.read(50)
            if not result == expected:
                LOG.info("Serial communication problem.")
                LOG.info("Expected %s got %s", expected, result)
                ser = None
        except serial.SerialException:
            LOG.info("Serial connection to %s failed", port)
        return ser