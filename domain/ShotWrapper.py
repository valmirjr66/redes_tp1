import json
from domain.NetworkInterface import NetworkInterface

class ShotWrapper:
    def __init__(self, network_interface: NetworkInterface):
        self.content = []
        self.network_interface = network_interface
        

    def get_content(self):
        return self.content