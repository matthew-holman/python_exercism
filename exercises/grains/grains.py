CHESSBOARD_SQUARES = 64


def square(number: int) -> int:
    if not 0 < number <= CHESSBOARD_SQUARES:
        raise ValueError("square must be between 1 and 64")
    # sequence doubles each square after the first square which is 1
    # 1 -> 1
    # 2 -> 2
    # 3 -> 4
    # 4 -> 8
    # 5 -> 16
    # 6 -> 32
    # 7 -> 64
    # the number for any given square is 2 (doubling each square) to the power of the previous
    # square number, the exponent (number - 1) informs haw many times the doubling has occurred
    # since the first square
    return 2 ** (number - 1)


def total() -> int:
    # total is the sum of all squares (2 to the power of square number - 1)
    # 2⁰ + 2¹ + 2² + ... + 2⁶³
    # this is a geometric series from 0 to 63
    return (2**CHESSBOARD_SQUARES) - 1
