from tictacai.game.engine import TicTacToe
from tictacai.game.players import RandomComputerPlayer
from tictacai.logic.models import Mark

from console.renderers import ConsoleRenderer

player1 = RandomComputerPlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

tictactoe = TicTacToe(playerOne=player1, playerTwo=player2, renderer=ConsoleRenderer())

tictactoe.play()
