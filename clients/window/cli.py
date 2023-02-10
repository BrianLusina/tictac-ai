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
    playerOne = WindowPlayer(Mark("X"), events)
    playerTwo = MinimaxComputerPlayer(Mark("O"))
    starting_mark = Mark("X")
    TicTacToe(playerOne=playerOne, playerTwo=playerTwo, renderer=WindowRenderer(window)).play(starting_mark)
