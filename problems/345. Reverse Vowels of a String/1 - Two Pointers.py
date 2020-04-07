class Solution:
    """
    https://leetcode.com/problems/reverse-vowels-of-a-string/discuss/567723/Two-pointers-technique-(Python-O(n)-time-and-space)
    Time: O(n)
    Space: O(n)
    """
    def reverseVowels(self, s: str) -> str:
        vowels = {"AaEeIiOoUu"}
        data = list(s)
        p1, p2 = 0, len(data) - 1
        while p1 < p2:
            if data[p1] in vowels and data[p2] in vowels:
                data[p1], data[p2] = data[p2], data[p1]
                p1 += 1
                p2 -= 1

            if data[p1] not in vowels:
                p1 += 1

            if data[p2] not in vowels:
                p2 -= 1

        return "".join(data)
