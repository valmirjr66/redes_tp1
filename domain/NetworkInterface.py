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
            return socket_response
        except timeout:
            print("Command " + command + " timed out, trying again.")


class NetworkInterface:
    def __init__(self, sag, socket_instances):
        self.sag = sag
        self.socket_instances = socket_instances

    def authenticate(self):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(socket_instance, self.sag, "authreq"))
        return response

    def get_cannons(self):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(
                socket_instance, self.sag, "getcannons"))
        return response

    def quit_game(self):
        response = []
        for socket_instance in self.socket_instances:
            response.append(send_command(socket_instance, self.sag, "quit"))
        return response

    def close_all_sockets(self):
        for socket_instance in self.socket_instances:
            socket_instance.close()
