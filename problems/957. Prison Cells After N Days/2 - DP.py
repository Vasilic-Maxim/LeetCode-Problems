from typing import List


class Solution:
    """
    Explanation:
        First lents see how the sequence will evolve
        after several iterations:

        Day 0    0	1	0	1	1	0	0	1
        -------------------------------------
        Day 1    0	1	1	0	0	0	0	0
        Day 2    0	0	0	0	1	1	1	0
        Day 3    0	1	1	0	0	1	0	0
        Day 4    0	0	0	0	0	1	0	0
        Day 5    0	1	1	1	0	1	0	0
        Day 6    0	0	1	0	1	1	0	0
        Day 7    0	0	1	1	0	0	0	0
        Day 8    0	0	0	0	0	1	1	0
        Day 9    0	1	1	1	0	0	0	0
        Day 10   0	0	1	0	0	1	1	0
        Day 11   0	0	1	0	0	0	0	0
        Day 12   0	0	1	0	1	1	1	0
        Day 13   0	0	1	1	0	1	0	0
        Day 14   0	0	0	0	1	1	0	0
        -------------------------------------
        Day 15   0	1	1	0	0	0	0	0
        Day 16   0	0	0	0	1	1	1	0
        Day 17   0	1	1	0	0	1	0	0
        ...

        Observations:
        First, initial sequence is unique if and only
        if first or last element in the sequence is
        '1'. In case if it is unique we change the
        sequence once to drop that property.

        Second, each 14 days, after dropping the
        uniqueness, the pattern starts to repeat.

        Conclusion:
        If the sequence is unique that we have to drop
        that property because it will not be path of
        pattern. Next we have to compute the real number
        of changes we have to make.

    Time: O(m + m * mod(n - 1, 14)) => O(m)
    Space: O(1)
    """

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # drop uniqueness if it exist
        if cells[0] or cells[-1]:
            self.next_day(cells)
            cells[0] = cells[-1] = 0
            n -= 1

        # compute the number of real changes
        n %= 14

        # make real changes
        for _ in range(n):
            self.next_day(cells)

        return cells

    def next_day(self, cells: List[int]):
        prev = cells[0]
        for i in range(1, len(cells) - 1):
            tmp = cells[i]
            cells[i] = int(prev == cells[i + 1])
            prev = tmp
