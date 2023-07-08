import unittest

from solution import solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(
            solution(
                [
                    [0, 2, 1, 0, 0],
                    [0, 0, 0, 3, 4],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ]
            ),
            [7, 6, 8, 21],
        )
        self.assertEqual(
            solution(
                [
                    [0, 1, 0, 0, 0, 1],
                    [4, 0, 0, 3, 2, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ),
            [0, 3, 2, 9, 14],
        )
        self.assertEqual(
            solution(
                [
                    [0, 1, 0, 0, 0, 1],
                    [4, 0, 0, 3, 2, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ),
            [0, 3, 2, 9, 14, 0],
        )
        self.assertEqual(solution([[0]]), [1, 1])

    def test_singular_matrix(self):
        with self.assertRaises(ValueError):
            solution([[0, 1], [0, 0]])


if __name__ == "__main__":
    unittest.main()
