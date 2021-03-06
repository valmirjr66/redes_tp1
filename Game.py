from domain.CannonsWrapper import CannonsWrapper
from domain.NetworkInterface import NetworkInterface
from domain.TurnWrapper import TurnWrapper


def execute_game_logic(net_interface: NetworkInterface):
    net_interface.authenticate()

    cannons_wrapper = CannonsWrapper(
        net_interface.get_cannons())

    if not cannons_wrapper.validate_cannons():
        print("cannons have bad positioning, finishing game")
        net_interface.quit_game()
        return 1

    turn_wrapper = TurnWrapper(net_interface)

    turn_wrapper.get_next_turn()

    for turn_number in range(0, 273):
        print("starting turn " + str(turn_number))

        for river in range(1, 5):
            state = turn_wrapper.get_state_by_river(river)

            for ship in state['ships']:
                best_cannon = cannons_wrapper.get_best_cannon_for_shot(
                    river, state['bridge'])

                if best_cannon != None:
                    response = net_interface.shot(river, best_cannon, ship['id'])
                    print(response)

        turn_wrapper.get_next_turn()

        if turn_wrapper.is_game_over():
            print("we lost, finishing game")
            net_interface.quit_game()
            break

    net_interface.quit_game()

    return 0


class Game:
    def __init__(self, net_interface):
        self.net_interface = net_interface

    def play_game(self):
        execute_game_logic(self.net_interface)
