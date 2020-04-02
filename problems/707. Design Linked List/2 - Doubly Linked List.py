class Node:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def getNode(self, index: int):
        if index <= self.len // 2 + self.len % 2 - 1:
            return self.getFromLeft(index)
        return self.getFromRight(index)

    def getFromLeft(self, index: int):
        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        return pointer

    def getFromRight(self, index: int):
        pointer = self.tail
        for _ in range(self.len - index - 1):
            pointer = pointer.prev

        return pointer

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1

        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.len, val)

    def linkNodes(self, left: Node, right: Node) -> None:
        if left is not None:
            left.next = right
        if right is not None:
            right.prev = left

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return

        left = right = None
        if index in range(self.len):
            right = self.getNode(index)
            left = right.prev
        elif index:
            left = self.tail

        node = Node(val, left, right)
        self.linkNodes(left, node)
        self.linkNodes(node, right)

        if left is None:
            self.head = node
        if right is None:
            self.tail = node

        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return

        node = self.getNode(index)
        left, right = node.prev, node.next
        self.linkNodes(left, right)

        if node is self.head:
            self.head = right
        if node is self.tail:
            self.tail = left

        self.len -= 1
