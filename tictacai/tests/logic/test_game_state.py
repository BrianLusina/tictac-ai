import unittest
from tictacai.logic.models import Grid, GameState, Mark, Move


class GameStateTestCases(unittest.TestCase):
    def test_game_not_started_returns_correct_value_on_initial_game_state(
        self,
    ):
        """Initial GameState should have game_not_started as True"""
        game_state = GameState(Grid())
        self.assertTrue(game_state.game_not_started)

    def test_game_over_returns_correct_value_on_initial_game_state(self):
        """Initial GameState should have game_over as False"""
        game_state = GameState(Grid())
        self.assertFalse(game_state.game_over)

    def test_game_tie_returns_correct_value_on_initial_game_state(self):
        """Initial GameState should have game_tie as False"""
        game_state = GameState(Grid())
        self.assertFalse(game_state.tie)

    def test_winner_returns_correct_value_on_initial_game_state(self):
        """Initial GameState should have winner as None"""
        game_state = GameState(Grid())
        self.assertIsNone(game_state.winner)

    def test_winning_cells_returns_correct_value_on_initial_game_state(self):
        """Initial GameState should have winning_cells as empty"""
        game_state = GameState(Grid())
        self.assertEqual([], game_state.winning_cells)

    def test_concluded_game_state_returns_correct_marks_and_winner(self):
        """Concluded GameState should return correct Marks, winner & winning cells"""
        game_state = GameState(Grid("XOXOXOXXO"), starting_mark=Mark("X"))

        expected_starting_mark = Mark.CROSS
        actual_staring_mark = game_state.starting_mark
        self.assertEqual(expected_starting_mark, actual_staring_mark)

        expected_current_mark = Mark.NAUGHT
        actual_current_mark = game_state.current_mark
        self.assertEqual(expected_current_mark, actual_current_mark)

        expected_winner = Mark.CROSS
        actual_winner = game_state.winner
        self.assertEqual(expected_winner, actual_winner)

        expected_winning_cells = [2, 4, 6]
        actual_winning_cells = game_state.winning_cells
        self.assertEqual(expected_winning_cells, actual_winning_cells)

    def test_in_progress_game_state_returns_correct_possible_moves(self):
        """In Progress GameState should return correct possible moves"""
        game_state = GameState(Grid("XXOXOX  O"))

        expected_possible_moves = [
            Move(
                mark=Mark.NAUGHT,
                cell_index=6,
                before_state=GameState(
                    grid=Grid(cells="XXOXOX  O"), starting_mark=Mark.CROSS
                ),
                after_state=GameState(
                    grid=Grid(cells="XXOXOXO O"), starting_mark=Mark.CROSS
                ),
            ),
            Move(
                mark=Mark.NAUGHT,
                cell_index=7,
                before_state=GameState(
                    grid=Grid(cells="XXOXOX  O"), starting_mark=Mark.CROSS
                ),
                after_state=GameState(
                    grid=Grid(cells="XXOXOX OO"), starting_mark=Mark.CROSS
                ),
            ),
        ]
        actual_possible_moves = game_state.possible_moves
        self.assertEqual(expected_possible_moves, actual_possible_moves)


if __name__ == "__main__":
    unittest.main()
