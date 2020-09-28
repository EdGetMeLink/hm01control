"""
grbl Class
"""
import logging

LOG = logging.getLogger(__name__)


class ConnectionError(Exception):
    pass


class Grbl:
    """
    grbl class for sending and receiving commands towards grbl
    """

    def __init__(self, connection, device=None, speed=115200, host=None, tcp_port=None):
        """
        grbl connection class connects to a grbl board over serial port
        :param str device: the serial device to use default /dev/null
        :param int speed: the speed to set the serial port to
        :param int tcp_port: the tcp port to connect to if device is tcp
        """
        self.connection = connection
        self.device = device
        self.speed = speed
        self.host = host
        self.tcp_port = tcp_port

    def connect(self, retry=2):
        """
        connect to grbl controller
        :param int retry: retries n times to connect to grbl
        :raises ConnectionError: if no connection to the grbl board occurs after retry count
        """
        if device == "tcp":
            conenctor = tcpserial.Tcp2Serial()
        else:
            connector 
        for count in range(retry):
            self.serial = grbl_serial(self.port, self.speed)
            if self.serial:
                break
        if not self.serial:
            raise ConnectionError(
                "could not connect to grbl board after %s tries", count
            )

        LOG.info("Connection to grbl board done")

    def get_grbl_config(self):
        """"
        get config of the grbl board
        """
        self.connection.send("$$")
        self.connection.read()
        ret = {
            0:10,
            1:25,
            2:0
        }
        return ret


