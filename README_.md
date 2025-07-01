
# 🚀 LeetCode Solutions: Arrays & Linked Lists (Python)

This repository includes clean and efficient Python solutions to selected LeetCode problems in the categories of **Arrays** and **Linked Lists**. Each problem is documented with explanation, code, and complexity analysis.

---


## 🔢 Problem 1: Two Sum

**LeetCode ID:** [1. Two Sum](https://leetcode.com/problems/two-sum/)  
**Category:** Array  
**Difficulty:** Easy

### 📝 Description

> Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

Each input has **exactly one solution**, and you **may not use the same element twice**.

---

### ✅ Solution (Python)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Stores number and index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
```

---

### 📈 Example

```python
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]
Explanation: 2 + 7 = 9
```


---

### 🧮 Complexity

| Metric           | Value  |
|------------------|--------|
| Time Complexity  | O(n)   |
| Space Complexity | O(n)   |

---

## 🔗 Problem 2: Add Two Numbers

**LeetCode ID:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)  
**Category:** Linked List  
**Difficulty:** Medium

### 📝 Description

> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

The input numbers **do not contain leading zeros**, except for the number 0 itself.

---

### ✅ Solution (Python)

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
```

---

### 📈 Example

```python
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]  
Output: [7, 0, 8]
Explanation: 342 + 465 = 807
```

---

### 🧮 Complexity

| Metric           | Value           |
|------------------|------------------|
| Time Complexity  | O(max(n, m))     |
| Space Complexity | O(max(n, m))     |

---

## 📂 Suggested GitHub Structure

```
leetcode/
├── array/
│   └── 001_two_sum.py
├── linked_list/
│   └── 002_add_two_numbers.py
└── README.md
```

---

## 🏁 Author

**Muhammad Saeed**  
- Passionate about AI, Machine Learning, and Problem Solving  
- GitHub: [@your_github_username](https://github.com/your_github_username)  
- LeetCode: [@your_leetcode_username](https://leetcode.com/your_leetcode_username)

---

## ⭐ If you found this helpful, please give a star!
