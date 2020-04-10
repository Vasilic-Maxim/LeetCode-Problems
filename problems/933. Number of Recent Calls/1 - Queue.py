from collections import deque


class RecentCounter:
    """
    Time: O(n)
    Space: O(n)
    """
    def __init__(self):
        self.data = deque()

    def ping(self, t: int) -> int:
        self.data.append(t)
        while self.data[0] < t - 3000:
            self.data.popleft()
        return len(self.data)
