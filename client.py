#!/usr/bin/env python3

import socket
import sys
from time import sleep

from domain.NetworkInterface import NetworkInterface
from Game import Game

HOSTNAME = sys.argv[1]
PORT = int(sys.argv[2])
SAG = sys.argv[3]

if len(sys.argv) != 4:
    raise Exception("Invalid input format.")

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_1.settimeout(2)
socket_2.settimeout(2)
socket_3.settimeout(2)
socket_4.settimeout(2)

socket_1.bind(('', 0))
socket_2.bind(('', 0))
socket_3.bind(('', 0))
socket_4.bind(('', 0))

socket_1.connect((HOSTNAME, PORT))
socket_2.connect((HOSTNAME, PORT+1))
socket_3.connect((HOSTNAME, PORT+2))
socket_4.connect((HOSTNAME, PORT+3))

net_interface = NetworkInterface(
    SAG, [socket_1, socket_2, socket_3, socket_4])

game_instance = Game(net_interface)
status = game_instance.play_game()
