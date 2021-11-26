import json
from struct import pack


def send_command(socket_instance, sag, command):
    raw_object = json.dumps(
        {"type": command, "auth":  sag})
    final_object = pack("!{}s".format(len(raw_object)),
                        raw_object.encode("utf-8"))

    socket_instance.sendall(final_object)

    socket_response = socket_instance.recv(1024).decode("utf-8")

    print(socket_response)


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
