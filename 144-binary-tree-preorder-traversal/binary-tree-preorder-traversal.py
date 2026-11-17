# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root,result=None):
        if result is None:
            result=[]
        if root is None:
            return result
        result.append(root.val)
        self.preorderTraversal(root.left,result)
        self.preorderTraversal(root.right,result)
        return result
        