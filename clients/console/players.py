import re

from tictacai.game.players import Player
from tictacai.logic.exceptions import InvalidMove
from tictacai.logic.models import GameState, Move

class ConsolePlayer(Player):
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark}'s move: ".strip()))
            except ValueError:
                print("Please provide coordinates in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied")
        return None
    

def grid_to_index(grid: str) -> int:
    """
    Takes in a cell position in the form of A1 or 1A and converts it into a grid position on the board.
    Regular expression are used to extract the numeric row and column so that calculation can be done
    to get the corresponding index in the flat sequence of cells
    :param grid cell position
    """
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Invalid grid coordinates")
    return 3 * (int(row) - 1) + (ord(col.upper())) - ord("A")
