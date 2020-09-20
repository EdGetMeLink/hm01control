"""
grbl Class
"""
import serial
import logging

LOG = logging.getLogger(__name__)


class ConnectionError(Exception):
    pass


class Grbl:
    """
    grbl class for sending and receiving commands towards grbl
    """

    def __init__(self, port="/dev/null", speed=115200):
        """
        grbl connection class connects to a grbl board over serial port
        :param str port: the serial port to use default /dev/null
        :param int speed: the speed to set the serial port to
        """
        self.port = port
        self.speed = speed

    def connect(self, retry=2):
        """
        connect to grbl controller
        :param int retry: retries n times to connect to grbl
        :raises ConnectionError: if no connection to the grbl board occurs after retry count
        """
        for count in range(retry):
            self.serial = grbl_serial(self.port, self.speed)
            if self.serial:
                break
        if not self.serial:
            raise ConnectionError(
                "could not connect to grbl board after %s tries", retry
            )

        LOG.info("Connection to grbl board done")

    def get_grbl_config(self):
        """"
        get config of the grbl board
        """
        self.send("$$")
        self.read()
        ret = {
            0:10,
            1:25,
            2:0
        }
        return ret


def grbl_serial(port: str, speed: int) -> serial.Serial:
    """
    serial wrapper function
    :param str port: serial port to use
    :param int speed: the speed to configure the serial port
    :return: serial Object or None
    """
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