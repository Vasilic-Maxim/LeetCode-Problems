class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node


class MyLinkedList:
    def __init__(self) -> None:
        self.head = None    # link to firs node in Linked List
        self.tail = None    # link to last node in Linked List
        self.len = 0        # length of Linked List

    def getNode(self, index) -> Node:
        if index == self.len - 1:
            # make your worst case the best
            return self.tail

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        return pointer

    def getPairOfNodes(self, index: int) -> tuple:
        left = self.getNode(index - 1) if index else None
        right = left.next if left is not None else self.head
        return left, right

    def linkNodes(self, left: Node, right: Node) -> None:
        if left is None:
            self.head = right
        else:
            left.next = right

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1

        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return

        left, right = self.getPairOfNodes(index)
        node = Node(val, right)
        self.linkNodes(left, node)

        if right is None:
            # in case when index is the same as the
            # length of the Linked List it means that
            # we a dealing with the last node
            self.tail = node

        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return

        left, right = self.getPairOfNodes(index)
        self.linkNodes(left, right.next)

        if right is self.tail:
            # assign new tail if it was deleted
            self.tail = left

        self.len -= 1
