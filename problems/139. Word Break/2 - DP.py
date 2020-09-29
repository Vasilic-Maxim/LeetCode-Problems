from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(n)
    """

    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        for i in range(n):
            if not dp[i]:
                continue

            for j in range(i, n):
                if s[i:j] in word_dict:
                    dp[j + 1] = True
                    break

        return dp[-1]
