class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def removeDuplicates(self, string: str) -> str:
        stack = []
        for char in string:
            if not stack or stack[-1] != char:
                stack.append(char)
            elif stack and stack[-1] == char:
                stack.pop()
        return "".join(stack)
