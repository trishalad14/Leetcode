# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i == l - 1:                 # last node of this level
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
        