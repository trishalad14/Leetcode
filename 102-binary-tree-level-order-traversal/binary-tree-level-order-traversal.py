# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        q=deque([root])
        result=[]
        while q:
            level=[]
            for _ in range(len(q)):
                root=q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            result.append(level)
        return result
        