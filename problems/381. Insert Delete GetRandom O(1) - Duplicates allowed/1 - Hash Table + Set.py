import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.positions = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.positions[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.nums) == 1

    def remove(self, val: int) -> bool:
        if not self.positions[val]:
            return False

        # take any position of value we are searching for
        remove_idx = self.positions[val].pop()
        last_idx = len(self.nums) - 1
        last_elm = self.nums[-1]

        # copy last element on position of element we
        # want to delete
        self.nums[remove_idx] = last_elm
        # add new position for copied element
        self.positions[last_elm].add(remove_idx)
        # delete last element's index from positions
        self.positions[last_elm].remove(last_idx)
        # Delete last element from the list that in any case
        # will be the element were searching for or space
        # we must get rid of
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

    def __present(self, val: int) -> bool:
        return len(self.positions[val]) > 0
