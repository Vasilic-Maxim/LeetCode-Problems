class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.root = None

    def connect(self, first: Node, second: Node) -> None:
        first.next = second
        second.prev = first

    def insert(self, left: Node, central: Node, right: Node):
        self.connect(left, central)
        self.connect(central, right)

    def extract(self, node: Node) -> Node:
        if node is self.root:
            self.root = self.root.next
        self.connect(node.prev, node.next)
        return node

    def append(self, node: Node) -> None:
        if self.root is None:
            self.connect(node, node)
            self.root = node
        else:
            self.insert(self.root.prev, node, self.root)

    def move_to_end(self, node: Node) -> None:
        if node is self.root:
            self.root = self.root.next
        elif node is not self.root.prev:
            self.append(self.extract(node))

    def popleft(self) -> Node:
        return self.extract(self.root)


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.least_used = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.least_used.move_to_end(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.least_used.move_to_end(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                node = self.least_used.popleft()
                del self.cache[node.key]

            node = Node(key, value)
            self.cache[key] = node
            self.least_used.append(node)
