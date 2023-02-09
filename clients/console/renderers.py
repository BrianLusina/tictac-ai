import textwrap
from typing import Iterable

from tictacai.game.renderers import Renderer
from tictacai.logic.models import GameState


class ConsoleRenderer(Renderer):
    def render(self, game_state: GameState) -> None:
        clear_screen()
        if game_state.winner:
            print_blinking(game_state.grid.cells, game_state.winning_cells)
            print(f"{game_state.winner} wins \N{party popper}")
        else:
            print_solid(game_state.grid.cells)
            if game_state.tie:
                print("No on wins this time \N{neutral face}")


def clear_screen() -> None:
    """
    Clears the current screen.

    The string literal "\033" represents a non-printable Esc character, which starts a special code sequence.
    The letter c that follows encodes the command to clear the screen. Note that the print() function automatically ends
    the text with a newline character. To avoid adding an unnecessary blank line, you must disable this by setting the
    end argument.
    """
    print("\033c", end="")


def blink(text: str) -> str:
    """
    Wraps the text in ANSI escape code.
    """
    return f"\033[5m{text}\033[0m"


def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    """
    This prints a blinking text of the winning cells by taking the current cells on the board & the positions of the
    winning cells. The winning cells are copied & rendering is delegated to print_solid
    :param cells: The current cells on the board
    :param positions: The positions to be rendered using blinking text
    :return:
    """
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)


def print_solid(cells: Iterable[str]) -> None:
    """
    Renders the tic-tac-toe grid with player's marks formatted in a multiline template string using the textwrap module
    to remove the indentation.
    Prints the sequence of cells with an additional gutter around the top left corner. It contains numbered rows & 
    columns indexed by letters. For example:
        A   B   C
      ------------
    1 ┆  X │ O │ X
      ┆ ───┼───┼───
    2 ┆  O │ O │
      ┆ ───┼───┼───
    3 ┆    │ X │    
        
    :param cells sequence of sales from the grid
    """
    print(
        textwrap.dedent(
            """\
             A   B   C
           ------------
        1 ┆  {0} │ {1} │ {2}
          ┆ ───┼───┼───
        2 ┆  {3} │ {4} │ {5}
          ┆ ───┼───┼───
        3 ┆  {6} │ {7} │ {8}                
            """
        ).format(*cells)
    )
