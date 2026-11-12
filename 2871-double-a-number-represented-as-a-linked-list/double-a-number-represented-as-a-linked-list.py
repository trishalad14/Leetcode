# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):

        # Step 1: Reverse the linked list
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev

        # Step 2: Double each digit
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        curr = head

        while curr:
            m = curr.val * 2 + carry

            tail.next = ListNode(m % 10)
            tail = tail.next

            carry = m // 10
            curr = curr.next

        if carry:
            tail.next = ListNode(carry)

        # Step 3: Reverse the answer
        prev = None
        curr = dummy.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev