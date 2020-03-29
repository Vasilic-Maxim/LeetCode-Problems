class Solution:
    """
    Time: O(max(len(a), len(b)))
    Space: O(max(len(a), len(b))) - space for 'result' list
    """

    def addBinary(self, a: str, b: str) -> str:
        a_idx, b_idx = len(a) - 1, len(b) - 1
        result = []
        to_add = 0
        while a_idx >= 0 or b_idx >= 0 or to_add:
            x = int(a[a_idx]) if a_idx >= 0 else 0
            y = int(b[b_idx]) if b_idx >= 0 else 0
            s = x + y + to_add
            digit = s % 2  # 0 or 1
            to_add = s // 2  # 0 or 1
            result.append(str(digit))
            a_idx -= 1
            b_idx -= 1

        return ''.join(result[::-1])
