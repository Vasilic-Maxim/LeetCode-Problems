from typing import List


class Solution:
    def nextGreaterElement(self, targets: List[int], nums: List[int]) -> List[int]:
        links, stack = {}, []
        for i, num in enumerate(reversed(nums)):
            while stack and stack[-1] < num:
                stack.pop()

            links[num] = stack[-1] if stack else -1
            stack.append(num)

        return [links[x] for x in targets]
