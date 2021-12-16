import json


class CannonsWrapper:
    def __init__(self, raw_cannons):
        self.content = json.loads(raw_cannons)['cannons']

    def get_content(self):
        return self.content
