class Solution:
    """
    n - number of cells on the board
    Time: O(n)
    Space: O(n)
    """

    def isValidSudoku(self, board: list) -> bool:
        checked = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val != '.':
                    row = f"{val}r{i}"
                    col = f"{val}c{j}"
                    box = f"{val}b{i // 3}-{j // 3}"

                    if row in checked or col in checked or box in checked:
                        return False

                    checked.add(row)
                    checked.add(col)
                    checked.add(box)
        return True
