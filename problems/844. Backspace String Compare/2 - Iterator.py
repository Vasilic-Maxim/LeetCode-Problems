from itertools import zip_longest


class Solution(object):
    """
    n - len(first)
    m - len(second)
    Time: O(n + m)
    Space: O(1)
    """
    def backspaceCompare(self, first, second):
        return all(x == y for x, y in zip_longest(self.iterate(first), self.iterate(second)))

    def iterate(self, cipher):
        skip = 0
        for x in reversed(cipher):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x
