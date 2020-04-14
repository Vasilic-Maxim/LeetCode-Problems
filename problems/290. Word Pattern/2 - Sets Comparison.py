class Solution:
    """
    n - len(pattern)
    m - len(string)

    Time: O(n + m)
    Space: O(n + m)
    """
    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split()
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words)) and len(pattern) == len(words)
