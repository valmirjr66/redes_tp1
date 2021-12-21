import json

from domain.NetworkInterface import NetworkInterface


class TurnWrapper:
    def __init__(self, network_interface: NetworkInterface):
        self.content = []
        self.turno = -1
        self.network_interface = network_interface

    def get_next_turn(self):
        self.turno += 1
        self.content = []
        raw_turn = self.network_interface.get_turn(self.turno)

        for item in raw_turn:
            self.content.append(json.loads(item))

    def is_game_over(self):
        has_game_ended = False

        for item in self.content:
            has_game_ended = has_game_ended or item['type'] == 'gameover'

        return has_game_ended

    def get_ships_by_river(self, river):
        return self.content[river - 1]
