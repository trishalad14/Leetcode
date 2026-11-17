# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxPathSum(self, root):
        self.maxi = float('-inf')

        def height(node):
            if node is None:
                return 0

            l = max(0, height(node.left))
            r = max(0, height(node.right))

            self.maxi = max(self.maxi, l + r + node.val)

            return node.val + max(l, r)

        height(root)
        return self.maxi
