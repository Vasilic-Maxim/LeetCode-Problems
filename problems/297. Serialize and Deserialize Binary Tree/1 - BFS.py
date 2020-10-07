from collections import deque
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        nums = []
        q = root is not None and deque([root])
        while q:
            node = q.popleft()
            nums.append("#" if node is None else str(node.val))
            if node is not None:
                q.append(node.left)
                q.append(node.right)

        while nums and nums[-1] == "#":
            nums.pop()

        return " ".join(nums)

    def deserialize(self, data: str):
        if not data:
            return None

        nums = data.split()
        root = self.__create_node(nums, 0)
        q = deque([root])
        pointer = 1
        while pointer < len(nums):
            node = q.popleft()
            if node is not None:
                node.left = self.__create_node(nums, pointer)
                node.right = self.__create_node(nums, pointer + 1)
                q.append(node.left)
                q.append(node.right)
                pointer += 2

        return root

    def __create_node(self, nums: List[str], idx: int):
        if idx >= len(nums) or nums[idx] == "#":
            return None

        return TreeNode(int(nums[idx]))
