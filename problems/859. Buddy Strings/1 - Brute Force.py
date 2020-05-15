class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def buddyStrings(self, first: str, second: str) -> bool:
        if len(first) != len(second):
            return False

        if first == second and len(first) != len(set(first)):
            return True

        diff = [(f, s) for f, s in zip(first, second) if f != s]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
