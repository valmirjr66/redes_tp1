import json


class CannonsWrapper:
    def __init__(self, raw_cannons):
        self.content = []
        for item in raw_cannons:
            self.content.append(json.loads(item)['cannons'])

    def get_content(self):
        return self.content
