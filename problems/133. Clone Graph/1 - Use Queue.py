from collections import deque


class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []


class Solution:
    def cloneGraph(self, node: Node):
        if node is None:
            return

        queue = deque()
        queue.append(node)
        vertex_map = dict({node.val: Node(node.val)})

        while len(queue):
            elm = queue.popleft()

            for neighbor in elm.neighbors:
                if neighbor.val not in vertex_map:
                    vertex_map[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                vertex_map[elm.val].neighbors.append(vertex_map[neighbor.val])

        return vertex_map[node.val]
