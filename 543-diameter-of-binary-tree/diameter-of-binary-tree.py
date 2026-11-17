# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def height(node):
            

            if node is None:
                return 0

            l = height(node.left)
            r = height(node.right)

            self.diameter = max(self.diameter, l + r)

            return 1 + max(l, r)

        height(root)

        return self.diameter