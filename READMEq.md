
---

## 📁 `leetcode/linked_list/002_add_two_numbers.md`

```markdown
# 🔗 Problem: Add Two Numbers

**LeetCode Problem ID:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)  
**Difficulty:** Medium  
**Category:** Linked List, Math

---

## 📝 Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

> You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## 🧠 Approach

1. Initialize a dummy node and use a pointer `tail` to build the result list.
2. Use a `carry` variable to store values ≥10.
3. Traverse both linked lists:
   - Add corresponding digits and carry.
   - Create a new node with `(sum % 10)` and attach it.
   - Update carry as `(sum // 10)`.
4. After traversal, if there's a carry, add one final node.

---

## ✅ Code (Python 3)

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode()  # Dummy head
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
