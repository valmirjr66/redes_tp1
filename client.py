#!/usr/bin/env python3

import socket
import sys
from NetworkInterface import NetworkInterface

HOSTNAME = sys.argv[1]
PORT = int(sys.argv[2])
SAG = sys.argv[3]

if len(sys.argv) != 4:
    raise Exception("Invalid input format.")

socket_instance_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_instance_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_instance_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_instance_4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_instance_1.connect((HOSTNAME, PORT))
socket_instance_2.connect((HOSTNAME, PORT+1))
socket_instance_3.connect((HOSTNAME, PORT+2))
socket_instance_4.connect((HOSTNAME, PORT+3))

net_interface = NetworkInterface(
    SAG, [socket_instance_1, socket_instance_2, socket_instance_3, socket_instance_4])

net_interface.authenticate()
net_interface.get_cannons()
net_interface.close_all_sockets()
net_interface.quit_game()