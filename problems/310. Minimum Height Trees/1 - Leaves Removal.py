from typing import List, Set


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """ Time/Space: O(n) """

        # base case
        if n <= 2:
            return list(range(n))

        # create an adjacency list
        adj: List[Set[int]] = [set() for _ in range(n)]
        for [f, t] in edges:
            adj[f].add(t)
            adj[t].add(f)

        # find all the leaves
        leaves = [i for i in range(n) if len(adj[i]) == 1]

        # get closer to the center by deleting leaves level by level
        unseen = n
        while unseen > 2:
            unseen -= len(leaves)
            new_leaves = []
            for v in leaves:
                w = adj[v].pop()
                adj[w].remove(v)
                if len(adj[w]) == 1:
                    new_leaves.append(w)
            leaves = new_leaves

        return list(leaves)
