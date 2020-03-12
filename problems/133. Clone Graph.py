'''
https://leetcode.com/problems/clone-graph/

'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        if neighbors is None:
            neighbors = []

        self.val = val
        self.neighbors = neighbors

class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        
    def enQueue(self, val: Node) -> None:
        if self.head is None:
            self.head = self.tail = QueueNode(val)
        else:
            self.tail.next = QueueNode(val)
            self.tail = self.tail.next
    
    def deQueue(self) -> QueueNode:
        if self.head is None:
            return
        
        tmp = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = self.head

        return tmp.val
    
    def isEmpty(self) -> bool:
        return self.head is None

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return
        
        queue = Queue()
        queue.enQueue(node)
        vertexMap = dict({ node.val: Node(node.val) })
        
        while not queue.isEmpty():
            elm = queue.deQueue()
            
            for neighbor in elm.neighbors:
                if neighbor.val not in vertexMap:
                    vertexMap[neighbor.val] = Node(neighbor.val)
                    queue.enQueue(neighbor)
                vertexMap[elm.val].neighbors.append(vertexMap[neighbor.val])
        
        return vertexMap[node.val]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node1)
node2.neighbors.append(node3)
node3.neighbors.append(node2)
node3.neighbors.append(node4)
node4.neighbors.append(node3)
node4.neighbors.append(node1)
s = Solution()
s.cloneGraph(node1)