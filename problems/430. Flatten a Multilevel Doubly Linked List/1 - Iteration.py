class Node:
    def __init__(self, val, prev_node, next_node, child):
        self.val = val
        self.prev = prev_node
        self.next = next_node
        self.child = child


class Solution:
    """
    l - number of levels

    Time: O(n)
    Space: O(l)
    """

    def flatten(self, head: Node) -> Node:
        stack = []
        node = head
        while node is not None:
            if node.child is not None:
                if node.next is not None:
                    stack.append(node.next)
                self.union(node, node.child)
                node.child = None
            elif node.next is None and stack:
                self.union(node, stack.pop())
            node = node.next
        return head

    def union(self, first: Node, second: Node):
        first.next, second.prev = second, first
