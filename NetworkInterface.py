import json
from socket import socket, timeout
from struct import pack


def send_command(socket_instance: socket, sag, command):
    raw_object = json.dumps(
        {"type": command, "auth":  sag})
    final_object = pack("!{}s".format(len(raw_object)),
                        raw_object.encode("utf-8"))

    while True:
        try:
            socket_instance.sendall(final_object)
            socket_response_raw = socket_instance.recv(1024)
            socket_response = socket_response_raw.decode("utf-8")
            print(socket_response)
            break
        except timeout:
            print("Command " + command + " timed out, trying again.")


class NetworkInterface:
    def __init__(self, sag, socket_instances):
        self.sag = sag
        self.socket_instances = socket_instances

    def authenticate(self):
        for socket_instance in self.socket_instances:
            send_command(socket_instance, self.sag, "authreq")

    def get_cannons(self):
        for socket_instance in self.socket_instances:
            send_command(
                socket_instance, self.sag, "getcannons")

    def quit_game(self):
        for socket_instance in self.socket_instances:
            send_command(socket_instance, self.sag, "quit")

    def close_all_sockets(self):
        for socket_instance in self.socket_instances:
            socket_instance.close()
