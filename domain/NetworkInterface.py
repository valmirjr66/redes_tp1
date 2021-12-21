import json
from socket import socket, timeout
from struct import pack
from typing import List


def send_command(socket_instance: socket, sag, command, appendix=None):
    default_object = {"type": command, "auth":  sag}

    raw_object = json.dumps(default_object) if appendix is None else json.dumps(
        {**default_object, **appendix})

    final_object = pack("!{}s".format(len(raw_object)),
                        raw_object.encode("utf-8"))

    while True:
        try:
            socket_instance.sendall(final_object)
            socket_response_raw = socket_instance.recv(1024)
            socket_response = socket_response_raw.decode("utf-8")
            return socket_response
        except timeout:
            print("Command " + command + " timed out, trying again.")


class NetworkInterface:
    def __init__(self, sag, socket_instances: List[socket]):
        self.sag = sag
        self.socket_instances = socket_instances

    def authenticate(self):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(socket_instance, self.sag, "authreq"))
        return response

    def get_cannons(self):
        response = send_command(
            self.socket_instances[0], self.sag, "getcannons")
        return response

    def get_turn(self, turn):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(socket_instance,
                            self.sag, "getturn", {"turn": turn}))
        return response

    def shot(self, cannon, id):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(
                socket_instance, self.sag, "shot", {"cannon": cannon, "id": id}))
        return response

    def quit_game(self):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(socket_instance, self.sag, "quit"))
            socket_instance.close()

        return response
