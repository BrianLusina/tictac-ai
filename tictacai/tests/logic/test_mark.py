import unittest
from tictacai.logic.models import Mark


class ModelsTestCases(unittest.TestCase):
    def test_mark_can_get_other_mark_from_property(self):
        """Mark.other property retrieves the other mark from enum"""
        x_mark = Mark("X")
        expected = Mark("O")
        actual = x_mark.other
        self.assertEqual(expected, actual)

    def test_mark_is_instance_of_str(self):
        """Mark.other property retrieves the other mark from enum"""
        self.assertTrue(isinstance(Mark.CROSS, str))
        self.assertTrue(isinstance(Mark.NAUGHT, str))


if __name__ == "__main__":
    unittest.main()
