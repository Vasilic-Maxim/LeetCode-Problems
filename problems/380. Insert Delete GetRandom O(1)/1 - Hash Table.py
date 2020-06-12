import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False

        self.positions[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False

        # copy last element on position of element
        # you want to delete
        self.nums[self.positions[val]] = self.nums[-1]
        # set last element position to its copy
        # position (previously deleted element position)
        self.positions[self.nums[-1]] = self.positions[val]
        # delete last element from the list and from
        # positions dictionary
        self.nums.pop()
        del self.positions[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
