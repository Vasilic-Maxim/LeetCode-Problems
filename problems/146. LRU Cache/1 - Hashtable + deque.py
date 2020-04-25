from collections import deque


class LRUCache:
    """
    Time: O(1) - 'capacity' is constant
    Space: O(1)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least_used = deque(maxlen=capacity)

    def add_recently_used_key(self, key: int) -> None:
        if key in self.least_used:
            self.least_used.remove(key)

        self.least_used.append(key)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.add_recently_used_key(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            if self.cache[key] != value:
                self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.least_used.popleft()]

            self.cache[key] = value

        self.add_recently_used_key(key)
