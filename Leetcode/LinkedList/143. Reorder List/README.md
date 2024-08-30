## 143. Reorder List
🔗  Link: [Reorder List](https://leetcode.com/problems/reorder-list/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Linked List, Two Pointers, Stack, Recursion<br>

=======================================================================================<br>

You are given the head of a singly linked-list. The list can be represented as:<br>

L0 → L1 → … → Ln - 1 → Ln<br>
Reorder the list to be on the following form:<br>

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …<br>
You may not modify the values in the list's nodes. Only nodes themselves may be changed.<br>

Example 1:<br>
Input: head = [1,2,3,4]<br>
Output: [1,4,2,3]<br>

Example 2:<br>
Input: head = [1,2,3,4,5]<br>
Output: [1,5,2,4,3]<br>
 

Constraints:<br>
The number of nodes in the list is in the range `[1, 5 * 104]`.<br>
`1 <= Node.val <= 1000<br>`
=======================================================================================<br>
### Evaluate
Assume n represents the number of nodes in the linked list.<br>
1. Reverse Linked List<br>
- Time Complexity: O(n)<br>
- Space Complexity: O(1)<br>

2. Deque<br>
- Time Complexity: O(n)<br>
- Space Complexity: O(n)<br>
