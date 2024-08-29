## 142. Linked List Cycle II
🔗  Link: [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Linked List, Hash table, Two pointer<br>

=======================================================================================<br>
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to **(0-indexed)**. It is `-1` if there is no cycle. **Note that `pos` is not passed as a parameter**.

**Do not modify** the linked list.


Example 1:<br>
Input: head = [3,2,0,-4], pos = 1<br>
Output: tail connects to node index 1<br>
Explanation: There is a cycle in the linked list, where tail connects to the second node.<br>

Example 2:<br>
Input: head = [1,2], pos = 0<br>
Output: tail connects to node index 0<br>
Explanation: There is a cycle in the linked list, where tail connects to the first node.<br>

Example 3:<br>
Input: head = [1], pos = -1<br>
Output: no cycle<br>
Explanation: There is no cycle in the linked list.<br>
 

Constraints:<br>
The number of the nodes in the list is in the range `[0, 104]`.<br>
`-105 <= Node.val <= 105`<br>
`pos` is `-1` or a valid index in the linked-list.<br>

=======================================================================================<br>
### Evaluate
Assume n represents the number of nodes in the linked list.
1. Use two pointer
- Time Complexity: O(n)
- Space Complexity: O(1)

2. Use hash table
- Time Complexity: O(n)
- Space Complexity: O(n)
