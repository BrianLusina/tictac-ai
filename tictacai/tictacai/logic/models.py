from __future__ import annotations
import enum
import re
from dataclasses import dataclass
from functools import cached_property


class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Mark:
        return Mark.NAUGHT if self is Mark.CROSS else Mark.NAUGHT


@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self) -> None:
        if not re.match(r'^[\sXO]{9}$', self.cells):
            raise ValueError("Must contain 9 cells of: X, O or space")

    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")

    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")
