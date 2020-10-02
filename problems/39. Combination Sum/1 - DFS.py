from typing import List


class Solution:
    """
    n = len(candidates)
    t = target
    Time: O(n ** t)
    Space: O(t)
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []

        def dfs(idx: int, path: List[int], path_sum: int) -> None:
            if not path_sum:
                result.append(path[:])
            else:
                for i in range(idx, n):
                    if path_sum < candidates[i]:
                        return

                    path.append(candidates[i])
                    dfs(i, path, path_sum - candidates[i])
                    path.pop()

        dfs(0, [], target)
        return result
