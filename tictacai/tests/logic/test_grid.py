import unittest
from tictacai.logic.models import Grid


class ModelsTestCases(unittest.TestCase):
    def test_new_grid_has_9_empty_spaces(self):
        """Grid instance should have 9 empty spaces"""
        grid = Grid()
        actual = grid.cells
        expected = 9
        self.assertTrue(expected, len(actual))

    def test_grid_contains_a_particular_cell_combination(self):
        """Grid instance should contain a particular cell combination"""
        grid = Grid("XXOXO O  ")
        actual = grid.cells
        expected = "XXOXO O  "
        self.assertTrue(expected, actual)

    def test_grid_is_not_created_with_too_few_cells(self):
        """Grid instance should not be created with too few cells"""
        with self.assertRaises(ValueError) as ex:
            Grid("XX")

        expected = "Must contain 9 cells of: X, O or space"
        self.assertEqual(expected, ex.exception.args[0])

    def test_grid_is_not_created_with_invalid_characters(self):
        """Grid instance should not be created with invalid characters"""
        with self.assertRaises(ValueError) as ex:
            Grid("XXOxO O  ")

        expected = "Must contain 9 cells of: X, O or space"
        self.assertEqual(expected, ex.exception.args[0])

    def test_grid_can_get_the_count_of_Xs_and_Os_and_empty(self):
        """Grid can get the correct count for Xs and Os & empty Slots"""
        grid = Grid("OXXXXOOOX")
        actual_x_count = grid.x_count
        expected_x_count = 5
        actual_o_count = grid.o_count
        expected_o_count = 4
        actual_empty_count = grid.empty_count
        expected_empty_count = 0

        self.assertEqual(expected_x_count, actual_x_count)
        self.assertEqual(expected_o_count, actual_o_count)
        self.assertEqual(expected_empty_count, actual_empty_count)


if __name__ == "__main__":
    unittest.main()
