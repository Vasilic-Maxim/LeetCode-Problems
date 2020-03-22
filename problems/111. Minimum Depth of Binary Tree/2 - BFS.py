'''
n - number of nodes in tree
Time: O(n)
Space: O(n)

Even thought we use some extra space to store the nodes in queue this algorithm
will bit DFS because it will emediatly will return the result after it will find
first leaf in tree. For DFS to traverse whole tree is needed.
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        
        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left is None and node.right is None:
                    return depth
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)