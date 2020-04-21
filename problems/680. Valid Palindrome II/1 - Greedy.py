class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def validPalindrome(self, pal: str) -> bool:
        for i in range(len(pal) // 2):
            if pal[i] != pal[~i]:
                return self.validate(pal, i + 1, len(pal) + ~i) or\
                       self.validate(pal, i, len(pal) + ~i - 1)

        return True

    @staticmethod
    def validate(pal, left, right):
        while left < right:
            if pal[left] != pal[right]:
                return False
            left += 1
            right -= 1
        return True
