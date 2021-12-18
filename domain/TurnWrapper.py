import json


class TurnWrapper:
    def __init__(self, raw_turn):
        print(raw_turn)
        self.content = []
        self.turno = 0

    def get_content(self):
        return self.content
