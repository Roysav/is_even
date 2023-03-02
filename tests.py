import unittest
from is_even import EvenNumber


class Tests(unittest.TestCase):
    cases = (
        (-10, True),
        (-9, False),
        (-8, True),
        (-7, False),
        (-6, True),
        (-5, False),
        (-4, True),
        (-3, False),
        (-2, True),
        (-1, False),
        (0, True),
        (1, False),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (6, True),
        (7, False),
    )

    def test_even(self):
        for number, expected in self.cases:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(isinstance(number, EvenNumber), expected)


if __name__ == '__main__':
    unittest.main()
