class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "R":
                x += 1
            else:
                x -= 1

        return x == y == 0
