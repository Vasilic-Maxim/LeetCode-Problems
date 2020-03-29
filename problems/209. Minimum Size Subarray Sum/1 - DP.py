class Solution:
    """
    Steps to solve the problem:
    -   find any sublist what matches the condition
    -   while sum of sublist matches the condition identify new
        minimum sublist length and subtract left elements from it
    -   repeat until the right pointer is out of list indices

    Time: O(n) -    we have two pointers since that we can visit an element
                    of the list just twice
    Space: O(1)
    """

    def minSubArrayLen(self, s: int, nums: list) -> int:
        min_sub = float('inf')
        left = right = sub_sum = 0
        while right < len(nums):
            sub_sum += nums[right]
            right += 1

            while sub_sum >= s:
                min_sub = min(min_sub, right - left)
                sub_sum -= nums[left]
                left += 1

        return min_sub if min_sub != float('inf') else 0
