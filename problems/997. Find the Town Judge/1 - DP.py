from typing import List


class Solution:
    """
    m - len(trusted_persons)
    Time: O(m + n)
    Space: O(n)
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counter = [0] * (n + 1)
        for citizen, trusted in trust:
            trust_counter[citizen] -= 1
            trust_counter[trusted] += 1

        for person in range(1, len(trust_counter)):
            if trust_counter[person] == n - 1:
                return person

        return -1
