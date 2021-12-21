import json

from domain.NetworkInterface import NetworkInterface


class TurnWrapper:
    def __init__(self, network_interface: NetworkInterface):
        self.content = []
        self.turno = 0
        self.network_interface = network_interface

        raw_turn = network_interface.get_turn(self.turno)

        for item in raw_turn:
            self.content.append(json.loads(item)['ships'])

    def get_content(self):
        return self.content

    def get_next_turn(self):
        self.turno += 1
        self.content = []
        raw_turn = self.network_interface.get_turn(self.turno)

        for item in raw_turn:
            self.content.append(json.loads(item))
