#!/usr/bin/env python3

import socket
import sys
from domain.CannonsWrapper import CannonsWrapper
from domain.NetworkInterface import NetworkInterface
from domain.TurnWrapper import TurnWrapper

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

socket_1.connect((HOSTNAME, PORT))
socket_2.connect((HOSTNAME, PORT+1))
socket_3.connect((HOSTNAME, PORT+2))
socket_4.connect((HOSTNAME, PORT+3))

net_interface = NetworkInterface(
    SAG, [socket_1, socket_2, socket_3, socket_4])

net_interface.authenticate()  # autentaticacao

cannons_wrapper = CannonsWrapper(
    net_interface.get_cannons())  # carrega canhoes

turn_wrapper = TurnWrapper(net_interface)  # carrega turno
for i in range(0, 270):
    turn_wrapper.get_next_turn()
    turn_current_content = turn_wrapper.get_content()
    has_game_ended = False

    for item in turn_current_content:
        has_game_ended = has_game_ended or item['type'] == 'gameover'

    if has_game_ended:
        break

net_interface.quit_game()
net_interface.close_all_sockets()
