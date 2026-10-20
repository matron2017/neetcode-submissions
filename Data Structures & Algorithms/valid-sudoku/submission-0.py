class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        columns = len(board[0])

        for i in range(rows):
            past = set()
            for j in range(columns):
                if board[i][j] in past:
                    return False
                elif board[i][j] != ".":
                    past.add(board[i][j])

        for j in range(columns):
            past = set()
            for i in range(rows):
                if board[i][j] in past:
                    return False
                elif board[i][j] != ".":
                    past.add(board[i][j])

        starts = [(0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)]

        for i, j in starts:
            past = set()
            for row in range(i, i+3):
                for column in range(j, j+3):
                    if board[row][column] in past:
                        return False
                    elif board[row][column] != ".":
                        past.add(board[row][column])

        return True