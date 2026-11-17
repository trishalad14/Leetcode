# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
         
        def height(node):

            if node is None:

                return 0
            l=height(node.left)
            r=height(node.right)
            if abs(r-l)>1:
                return -1
            if l==-1 or r==-1:
                return -1
            return 1+max(l,r)
        return height(root)!=-1
        