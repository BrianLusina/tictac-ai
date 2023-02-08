"""
Contains Renderer which will be responsible for visualizing the grid
"""
from abc import ABCMeta, abstractmethod

from ..logic.models import GameState


class Renderer(metaclass=ABCMeta):
    @abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state"""
