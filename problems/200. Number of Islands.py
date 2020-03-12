'''
https://leetcode.com/problems/number-of-islands/
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count
            
    def bfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 \
            or i >= len(grid) \
            or j < 0 \
            or j >= len(grid[0]) \
            or grid[i][j] != '1':
            return
        
        grid[i][j] = 0 # Mark as visited cell
        
        self.bfs(grid, i - 1, j) # up
        self.bfs(grid, i + 1, j) # down
        self.bfs(grid, i, j - 1) # left
        self.bfs(grid, i, j + 1) # right