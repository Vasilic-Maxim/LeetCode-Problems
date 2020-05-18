class Solution:
    """
    n - len(s1)
    m - len(s2)
    Time: O(n + m)
    Space: O(1)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = [0] * 26
        for char in s1:
            counter_s1[ord(char) - ord('a')] += 1

        counter_s2 = [0] * 26
        for j, char in enumerate(s2):
            if j >= len(s1):
                counter_s2[ord(s2[j - len(s1)]) - ord('a')] -= 1

            counter_s2[ord(char) - ord('a')] += 1

            if counter_s1 == counter_s2:
                return True
        return False
