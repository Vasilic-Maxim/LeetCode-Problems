class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """
    def mySqrt(self, x: int) -> int:
        answer = x
        while answer * answer > x:
            answer = (answer + x // answer) // 2
        return answer
