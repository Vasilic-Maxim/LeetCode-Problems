from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """ Time/Space: O(n) """

        stack = []
        for asteroid in asteroids:
            while stack and asteroid < stack[-1] <= abs(asteroid):
                if stack.pop() == abs(asteroid):
                    break
            else:
                stack.append(asteroid)

        return stack
