class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        NOTE:
            Why the list for storing sums' count is length of 37?
            1 - max number of digits for numbers in
            range 1 <= n <= 10^4 will be 36 (for number 9999)
            2 - one additional spot for zero (0) to not do shifts

        Time: O(n)
        Space: O(n)
        """
        dp = {0: 0}
        counter = [0] * 37
        for num in range(1, n + 1):
            div, mod = divmod(num, 10)
            dp[num] = dp[div] + mod
            counter[dp[num]] += 1

        return counter.count(max(counter))
