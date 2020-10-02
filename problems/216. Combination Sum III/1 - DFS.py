from typing import List


class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        result = []
        end = min(target + 1, 10)

        def dfs(start: int, path: List[int], path_value: int) -> None:
            if len(path) == k:
                if not path_value:
                    result.append(path[:])
            else:
                for j in range(start, end):
                    if path_value < j:
                        return

                    path.append(j)
                    dfs(j + 1, path, path_value - j)
                    path.pop()

        if 0 < k < 10 and 0 < target <= 45:
            dfs(1, [], target)

        return result
