# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        stack=[]
        curr=root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)
            curr=curr.right
        return result

    
      