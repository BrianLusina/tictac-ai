"""
Engine of the game
"""
from dataclasses import dataclass
from typing import Callable, TypeAlias

from .players import Player
from .renderers import Renderer
from ..logic.validators import validate_players
from ..logic.exceptions import InvalidMove
from ..logic.models import GameState, Grid, Mark

ErrorHandler: TypeAlias = Callable[[Exception], None]


@dataclass(frozen=True)
class TicTacToe:
    """
    :param playerOne 1st player
    :param playerTwo 2nd Player
    :param renderer handles visualizing the game board
    :param error_handler is an optional ErrorHandler callback which is exposed to the clients(frontend) to allows the
    frontend to decide how to take care of an exception
    """

    playerOne: Player
    playerTwo: Player
    renderer: Renderer
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_players(self.playerOne, self.playerTwo)

    def play(self, starting_mark: Mark = Mark("X")) -> None:
        """
        The engine requests that the renderer update the view and then uses a pull strategy to advance the game by
        asking both players to make their moves in alternating rounds. These steps are repeated in an infinite loop
        until the game is over.
        """
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> Player:
        """
        GameState only knows about the current player’s mark, which can be either X or O, but it doesn’t know about the
        specific player objects that were assigned those marks. Therefore, the need to map the current mark to a player
        object using this helper method
        """
        if game_state.current_mark is self.playerOne.mark:
            return self.playerOne
        else:
            return self.playerTwo
