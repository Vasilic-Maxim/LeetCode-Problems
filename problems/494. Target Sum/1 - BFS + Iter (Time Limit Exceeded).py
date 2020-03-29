from collections import deque


class Solution:
    """
    Note: Time Limit Exceeded!

    While we iterate throughout the 'nums' list the queue becomes huge,
    O(2^N) where N is the length of the array, hence the solution
    becomes slower and less effective.

    N - length of the array
    Time: O(2^N)
    Space: O(N*2^N)
    """

    def findTargetSumWays(self, nums: list, target: int) -> int:
        q = deque()
        q.append(0)
        for num in nums:
            for _ in range(len(q)):
                elm = q.popleft()
                q.append(elm - num)
                q.append(elm + num)
        return sum([x for _ in range(len(q)) if (x := q.popleft() == target)])
