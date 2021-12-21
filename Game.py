from domain.CannonsWrapper import CannonsWrapper
from domain.NetworkInterface import NetworkInterface
from domain.ShotWrapper import ShotWrapper
from domain.TurnWrapper import TurnWrapper


def execute_game_logic(net_interface: NetworkInterface):
    net_interface.authenticate()  # autentaticacao

    cannons_wrapper = CannonsWrapper(
        net_interface.get_cannons())  # carrega canhoes

    if not cannons_wrapper.validate_cannons():
        print("cannons have bad positioning, finishing game")
        return 1

    turn_wrapper = TurnWrapper(net_interface)  # carrega turno

    for i in range(0, 270):
        turn_wrapper.get_next_turn()
        current_turn_content = turn_wrapper.get_content()
        has_game_ended = False

        shot_wrapper = ShotWrapper(net_interface)

        for item in current_turn_content:
            has_game_ended = has_game_ended or item['type'] == 'gameover'

        if has_game_ended:
            break

    net_interface.quit_game()
    net_interface.close_all_sockets()

    return 0


class Game:
    def __init__(self, net_interface):
        self.net_interface = net_interface

    def play_game(self):
        execute_game_logic(self.net_interface)
