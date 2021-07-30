from chesspy.core.pieces import Pieces


class Board:
    def __init__(self):
        self.squares = [[row + 8 * i for row in range(8)] for i in range(8)]
        self.board = []

    def set_up_board(self):
        for rank, square in enumerate(self.squares):
            if rank == 0:
                self.board.append([
                    Pieces.BROOK,
                    Pieces.BKNIGHT,
                    Pieces.BBISHOP,
                    Pieces.BQUEEN,
                    Pieces.BKING,
                    Pieces.BBISHOP,
                    Pieces.BKNIGHT,
                    Pieces.BROOK
                ])
            elif rank == 1:
                self.board.append([Pieces.BPAWN for _ in range(8)])
            elif rank == 6:
                self.board.append([Pieces.WPAWN for _ in range(8)])
            elif rank == 7:
                self.board.append([
                    Pieces.WROOK,
                    Pieces.WKNIGHT,
                    Pieces.WBISHOP,
                    Pieces.WQUEEN,
                    Pieces.WKING,
                    Pieces.WBISHOP,
                    Pieces.WKNIGHT,
                    Pieces.WROOK
                ])
            else:
                self.board.append([0 for _ in range(8)])
