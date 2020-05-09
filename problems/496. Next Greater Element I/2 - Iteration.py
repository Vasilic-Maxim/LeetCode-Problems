from typing import List


class Solution:
    def nextGreaterElement(self, targets: List[int], nums: List[int]) -> List[int]:
        links, stack = {}, []
        for num in nums:
            while stack and stack[-1] < num:
                links[stack.pop()] = num
            stack.append(num)

        return [links.get(x, -1) for x in targets]