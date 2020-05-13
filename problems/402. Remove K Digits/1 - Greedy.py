class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []
        for digit in num:
            # if the last element in the stack is bigger than
            # current element it means we found a peak and we
            # need to drop it
            while k and stack and int(digit) < int(stack[-1]):
                stack.pop()
                k -= 1

            # don't add leading zeros
            if stack or digit != "0":
                stack.append(digit)

        # if we still should get rid of some elements
        # then it must be the elements from the end of
        # the stack
        for _ in range(k):
            stack.pop()

        return "".join(stack) or "0"
