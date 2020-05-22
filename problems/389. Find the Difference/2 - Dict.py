class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def findTheDifference(self, s: str, t: str) -> str:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or not counter[char]:
                return char
            counter[char] -= 1
