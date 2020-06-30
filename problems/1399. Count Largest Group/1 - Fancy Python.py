from statistics import multimode


class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Elegant but not very efficient solution.
        1 - multiple transition between str and int types
        2 - 'multimode' is very complex method (uses sorting, grouping, etc.)
        """
        return len(multimode(sum(map(int, str(i))) for i in range(1, n+1)))
