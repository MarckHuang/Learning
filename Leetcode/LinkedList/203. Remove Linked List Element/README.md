## 203. Remove Linked List Element
🔗  Link: [Remove Linked List Element](https://leetcode.com/problems/remove-linked-list-elements/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Linked List, Recursion<br>

=======================================================================================<br>

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.<br
                                                                                                                                                >

Example 1:<br>
Input: head = [1,2,6,3,4,5,6], val = 6<br>
Output: [1,2,3,4,5]<br>

Example 2:<br>
Input: head = [], val = 1<br>
Output: []<br>

Example 3:<br>
Input: head = [7,7,7,7], val = 7<br>
Output: []<br>
 
Constraints:<br>
The number of nodes in the list is in the range [0, 10^4].<br>
1 <= Node.val <= 50<br>
0 <= val <= 50<br>

=======================================================================================<br>
### Evaluate

Assume n represents the number of nodes in the linked list.

Time Complexity: O(n)
Space Complexity: O(1)
