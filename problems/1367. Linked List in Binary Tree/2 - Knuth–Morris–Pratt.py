class Solution(object):

    def isSubPath(self, head, root):
        A, dp = [head.val], [0]
        i = 0
        node = head.next
        while node:
            while i and node.val != A[i]:
                i = dp[i - 1]
            i += node.val == A[i]
            A.append(node.val)
            dp.append(i)
            node = node.next

        def dfs(root, i):
            if not root: return False
            while i and root.val != A[i]:
                i = dp[i - 1]
            i += root.val == A[i]
            return i == len(dp) or dfs(root.left, i) or dfs(root.right, i)

        return dfs(root, 0)
