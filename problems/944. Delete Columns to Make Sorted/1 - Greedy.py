from typing import List


class Solution:
    def minDeletionSize(self, words: List[str]) -> int:
        def is_unsorted(col: str) -> bool:
            return any(col[i] > col[i + 1] for i in range(len(col) - 1))

        return sum(map(is_unsorted, zip(*words)))
