import unittest
from chesspy.core.pieces import Pieces
from chesspy.core.board import Board


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()

    def test_square_numbers(self):
        squares = [
            [0, 1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28, 29, 30, 31],
            [32, 33, 34, 35, 36, 37, 38, 39],
            [40, 41, 42, 43, 44, 45, 46, 47],
            [48, 49, 50, 51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60, 61, 62, 63],
        ]
        self.assertEqual(squares, self.board.squares)

    def test_board_position(self):
        board = [
            [Pieces.BROOK,
             Pieces.BKNIGHT,
             Pieces.BBISHOP,
             Pieces.BQUEEN,
             Pieces.BKING,
             Pieces.BBISHOP,
             Pieces.BKNIGHT,
             Pieces.BROOK],
            [Pieces.BPAWN for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [Pieces.WPAWN for _ in range(8)],
            [Pieces.WROOK,
             Pieces.WKNIGHT,
             Pieces.WBISHOP,
             Pieces.WQUEEN,
             Pieces.WKING,
             Pieces.WBISHOP,
             Pieces.WKNIGHT,
             Pieces.WROOK],
        ]
        self.board.set_up_board()
        self.assertEqual(self.board.board, board)

    def test_bitboard(self):
        pass


if __name__ == '__main__':
    unittest.main()
