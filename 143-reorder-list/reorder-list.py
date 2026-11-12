# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        curr=second
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        second=prev
        first=head
        while second:
            n1=first.next
            n2=second.next
            first.next=second
            second.next=n1
            first=n1
            second=n2