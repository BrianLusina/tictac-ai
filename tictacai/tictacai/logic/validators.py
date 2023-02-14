from __future__ import annotations
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game.players import Player
    from ..game.players_async import AsyncPlayer
    from .models import Grid, GameState, Mark

from .exceptions import InvalidGameState


def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O or space")


def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(
        game_state.grid, game_state.starting_mark, game_state.winner
    )


def validate_number_of_marks(grid: Grid) -> None:
    """
    At any time, the number of marks left by one player must be either the same or greater by exactly one compared to
    the number of marks left by the other player. Initially, there are no marks, so the number of Xs and Os is equal to
    zero. When the first player makes a move, they’ll have one more mark than their opponent. But, as soon as the other
    player makes their first move, the proportion evens out again, and so on.
    """
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong number of Xs and Os")


def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    """
    The player who left more marks on the grid is guaranteed to be the starting player. If not, then you know that
    something must have gone wrong.
    """
    if grid.x_count > grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Wrong starting mark")
    elif grid.o_count > grid.x_count:
        if starting_mark != "O":
            raise InvalidGameState("Wrong starting mark")


def validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None
) -> None:
    """
    A starting player has an advantage, so when they win, they’ll have left more marks than their opponent. Conversely,
    the second player is at a disadvantage, so they can only win the game by making an equal number of moves as the
    starting player.
    """
    if winner == "X":
        if starting_mark == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong number of Xs")
    elif winner == "O":
        if starting_mark == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Wrong number of Os")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Wrong number of Os")


def validate_players(playerOne: Player, playerTwo: Player) -> None:
    """
    Validates that both players have different marks
    """
    if playerOne.mark is playerTwo.mark:
        raise ValueError("Players must use different marks")


def validate_async_players(
    playerOne: AsyncPlayer, playerTwo: AsyncPlayer
) -> None:
    """
    Validates that both players have different marks
    """
    if playerOne.mark is playerTwo.mark:
        raise ValueError("Players must use different marks")
