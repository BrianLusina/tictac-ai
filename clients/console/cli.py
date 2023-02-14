from tictacai.game.engine import TicTacToe

from .args import parse_args
from .renderers import ConsoleRenderer


def main() -> None:
    player1, player2, starting_mark = parse_args()
    tic_tac_toe = TicTacToe(
        playerOne=player1, playerTwo=player2, renderer=ConsoleRenderer()
    )
    tic_tac_toe.play(starting_mark=starting_mark)
