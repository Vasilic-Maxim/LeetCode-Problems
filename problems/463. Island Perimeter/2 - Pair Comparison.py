"""
Steps:
- create a list of all rows and cols
- compare each row with itself, with prefix / postfix
- count all differences
"""
from operator import ne


class Solution:
    def islandPerimeter(self, grid):
        # one line equivalent:
        # return sum(sum(list(map(ne, [0] + row, row + [0]))) for row in grid + list(map(list, zip(*grid))))
        counter = 0
        for row in (grid + list(map(list, zip(*grid)))):
            counter += sum(map(ne, [0] + row, row + [0]))
        return counter



