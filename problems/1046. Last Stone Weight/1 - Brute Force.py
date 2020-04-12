from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(1)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        is_changed = True
        while len(stones) > 1:
            if is_changed:
                stones.sort()

            new_stone = stones.pop() - stones.pop()
            is_changed = bool(new_stone)
            if new_stone:
                stones.append(new_stone)
        return stones[0] if len(stones) else 0
