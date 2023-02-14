from dataclasses import dataclass

from .engine import ErrorHandler
from .players_async import AsyncPlayer
from .renderers import Renderer
from ..logic.exceptions import InvalidMove
from ..logic.models import GameState, Grid, Mark
from ..logic.validators import validate_async_players


@dataclass(frozen=True)
class AsyncTicTacToe:
    playerOne: AsyncPlayer
    playerTwo: AsyncPlayer
    renderer: Renderer
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_async_players(self.playerOne, self.playerTwo)

    async def play(self, starting_mark: Mark = Mark("X")) -> None:
        game_state = GameState(Grid(), starting_mark)

        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = await player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> AsyncPlayer:
        if game_state.current_mark is self.playerOne.mark:
            return self.playerOne
        else:
            return self.playerTwo
