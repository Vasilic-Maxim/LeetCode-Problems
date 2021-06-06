from collections import deque
from typing import List, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.q = deque()
        self.next = 0

    def insert(self, val):
        node = TreeNode(val) if val is not None else val
        if self.root is None:
            self.root = node
        else:
            if not self.next:
                self.q[0].left = node
            else:
                self.q[0].right = node
                self.q.popleft()
            self.next ^= 1

        if val is not None:
            self.q.append(node)

    def update(self, nums: List[Any]):
        for num in nums:
            self.insert(num)
