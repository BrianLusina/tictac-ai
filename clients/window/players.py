from queue import Queue

from tictacai.game.players import Player
from tictacai.logic.models import GameState, Mark, Move


class WindowPlayer(Player):
    def __init__(self, mark: Mark, events: Queue) -> None:
        super().__init__(mark)
        self.events = events

    def get_move(self, game_state: GameState) -> Move | None:
        index = self.events.get()
        try:
            return game_state.make_move_to(index)
        finally:
            self.events.task_done()
