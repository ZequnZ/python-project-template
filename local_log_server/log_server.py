"""
log_server.py

This module spins up a local UDP log server that can print logs to the console and optionally save them to a text file.
"""

import argparse
import os
import socket
import sys


def parse_arguments(args):
    parser = argparse.ArgumentParser(description="Print Logs")
    parser.add_argument(
        "--save",
        dest="save",
        action="store_true",
        help="Set flag to save logs to text file.",
    )
    parser.add_argument(
        "--no-save",
        dest="save",
        action="store_false",
        help="Set flag not to save logs to text file.",
    )
    parser.set_defaults(save=True)
    parser.add_argument(
        "--port",
        default=5091,
        help="Use flag to specify logger port (default 5091).",
        type=int,
    )

    return parser.parse_args()


def spin_up_log_server(udp_ip, udp_port, save=False):
    """Spin up  a local udp log server."""
    try:
        os.remove("logfile.txt")
    except Exception:
        pass

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
    sock.bind((udp_ip, udp_port))
    while True:
        # buffer size is 1024 bytes
        data = sock.recvfrom(1024)[0]
        print(data.decode("utf-8"))
        # write logs to file
        if save:
            with open("logfile.txt", "a") as log_file:
                log_file.write(data.decode("utf-8") + "\n")


if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])

    UDP_PORT = int(args.port)
    UDP_IP = "0.0.0.0"

    spin_up_log_server(UDP_IP, UDP_PORT, args.save)
