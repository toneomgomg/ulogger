# -*- coding: utf-8 -*-
"""UDP Logger class"""
from typing import Optional

import socket

DEFAULT_SERVER = "127.0.0.1"
DEFAULT_PORT = 5005


class UdpLogger:

    def __init__(
        self,
        channel: str,
        component: Optional[str] = None,
        server: Optional[str] = None,
        port: Optional[int] = None
    ) -> None:
        """Initiale UDP logger.

        Args:
            channel (str): Log channel
            server (Optional[str]): Server IP
            port (Optional[int]): Server port
        """
        self.channel = channel
        self.component = component

        if server is not None:
            self.server = server
        else:
            self.server = DEFAULT_SERVER

        if port is not None:
            self.port = port
        else:
            self.port = DEFAULT_PORT

    def _output(self, prefix: str, message: str) -> None:
        """Output message to server

        Args:
            prefix (str): Message prefix
            message (str): Message
        """
        msg = f"{self.channel}:{self.component if self.component is not None else ''}:[{prefix}] {message}".encode('utf-8')

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(msg, (self.server, self.port))

    def info(self, message: str) -> None:
        """Print info

        Args:
            message (str): Message
        """
        self._output("INFO", message)
