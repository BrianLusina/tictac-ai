from queue import Queue
from threading import Thread

from tictacai.game.engine import TicTacToe
from tictacai.game.players import MinimaxComputerPlayer
from tictacai.logic.models import Mark

from .players import WindowPlayer
from .renderers import Window, WindowRenderer


def main() -> None:
    events = Queue()
    window = Window(events)
    Thread(target=game_loop, args=(window, events), daemon=True).start()
    window.mainloop()


def game_loop(window: Window, events: Queue) -> None:
    player_one = WindowPlayer(Mark("X"), events)
    player_two = MinimaxComputerPlayer(Mark("O"))
    starting_mark = Mark("X")
    TicTacToe(
        playerOne=player_one, playerTwo=player_two, renderer=WindowRenderer(window)
    ).play(starting_mark)
