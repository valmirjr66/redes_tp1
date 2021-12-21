import json

from domain.CannonUnity import CannonUnity


class CannonsWrapper:
    def __init__(self, raw_cannons):
        self.content = []
        for item in json.loads(raw_cannons)['cannons']:
            self.content.append(CannonUnity(item))

    def validate_cannons(self):
        safe_rivers_list = []
        for item in self.content:
            safe_rivers_list += item.get_rivers_in_range()

        return len(set(safe_rivers_list)) == 4

    def get_best_cannon_for_shot(self, river, bridge):
        for item in self.content:
            if item.get_bridge() == bridge and river in item.get_rivers_in_range():
                return item.get_coordinates()

        return None
