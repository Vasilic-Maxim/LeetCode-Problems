class Solution(object):
    """
    Time: O(n)
    Space: O(n)
    """

    def hIndex(self, citations):
        n = len(citations)
        buckets = [0] * (n + 1)

        for num in citations:
            if num >= n:
                buckets[n] += 1
            else:
                buckets[num] += 1

        count = 0

        for i in reversed(range(n)):
            count += buckets[i]

            if count >= i:
                return i

        return 0
