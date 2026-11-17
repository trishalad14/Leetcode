# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from  collections import deque
class Solution(object):
    def largestValues(self, root):

        if root is None:
            return []
        result=[]
        q=deque([root])
        while q:
            s=len(q)
            maximum=float('-inf')
            for _ in range(s):
                node=q.popleft()
                maximum=max(maximum,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(maximum)
        return result


        