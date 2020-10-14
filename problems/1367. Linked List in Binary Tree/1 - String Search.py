from typing import List, Iterable


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def traverse_list(node: ListNode) -> Iterable:
            while node is not None:
                yield node.val
                node = node.next

        def traverse_tree(node: TreeNode, stack: List[int]) -> Iterable:
            if node is None:
                yield " ".join(map(str, stack))
            else:
                stack.append(node.val)
                yield from traverse_tree(node.left, stack)
                yield from traverse_tree(node.right, stack)
                stack.pop()

        sub_path = " ".join(map(str, traverse_list(head)))
        for path in traverse_tree(root, []):
            if sub_path in path:
                return True
        return False
