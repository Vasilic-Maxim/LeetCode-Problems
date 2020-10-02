from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = set()
        candidates.sort()

        def dfs(idx: int, path: List[int], path_sum: int) -> None:
            if not path_sum:
                result.add(tuple(path))
            else:
                for i in range(idx, n):
                    if path_sum < candidates[i]:
                        return

                    path.append(candidates[i])
                    dfs(i + 1, path, path_sum - candidates[i])
                    path.pop()

        dfs(0, [], target)
        return list(result)
