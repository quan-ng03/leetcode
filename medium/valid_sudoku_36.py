from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # This is a brute-forced approach, where I check each condition.

    # Check rows
    for row in board:
        dictionary = {}
        for i in range(len(row)):
            if row[i] in dictionary and row[i] != ".":
                return False
            else:
                dictionary[row[i]] = 0
    # Check columns
    for col in range(9):
        dictionary = {}
        for i in range(9):
            if board[i][col] in dictionary and board[i][col] != ".":
                return False
            else:
                dictionary[board[i][col]] = 0
    # Check 3x3 boxes
    for row in [0, 3, 6]:
        for col in [0, 3, 6]:
            dictionary = {}
            for i in range(3):
                for j in range(3):
                    if (
                        board[row + i][col + j] in dictionary
                        and board[row + i][col + j] != "."
                    ):
                        return False
                    else:
                        dictionary[board[row + i][col + j]] = 0
    return True
