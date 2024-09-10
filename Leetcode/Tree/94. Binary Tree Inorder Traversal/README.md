## 144. Binary Tree Inorder Traversal
🔗  Link: [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree, Binary Tree,  Stack, DFS<br>

=======================================================================================<br>
Given the root of a binary tree, return the inorder traversal of its nodes' values.<br>

 
Example 1:<br>
Input: root = [1,null,2,3]<br>
Output: [1,3,2]<br>

Example 2:<br>
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]<br>
Output: [4,2,6,5,7,1,3,9,8]<br>

Example 3:<br>
Input: root = []<br>
Output: []<br>

Example 4:<br>
Input: root = [1]<br>
Output: [1]<br>

 
Constraints:

The number of nodes in the tree is in the range `[0, 100]`.
`-100 <= Node.val <= 100`
=======================================================================================<br>
### Evaluate

Assume n represents the number nodes in tree.

- Time Complexity: O(n)
- Space Complexity: avg O(log n), worst O(n)
