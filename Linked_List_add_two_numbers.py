# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers represented by two linked lists.
        Digits are stored in reverse order, and each node contains a single digit.
        Return the sum as a linked list.
        """
        head = tail = ListNode()  # Start a new result list
        carry = 0

        while l1 or l2:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(carry % 10)
            carry //= 10

            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            tail.next = ListNode(carry)

        return head.next
