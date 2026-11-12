# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):


        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse the second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # step 3: compare both halves
        left = head
        right = prev                   # head of the reversed second half
        while right:                   # the second half is the shorter or equal one
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True          
        
        
        