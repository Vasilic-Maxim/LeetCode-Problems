'''
Time: O(k*n) - 'insert' will take O(n) time each iteration
Space: O(1)
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop());