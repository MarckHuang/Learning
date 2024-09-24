## 101. Symmetric Tree
🔗  Link: [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree, Binary Tree,BFS, DFS<br>

=======================================================================================<br>
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).<br>

Example 1:<br>
Input: root = [1,2,2,3,4,4,3]<br>
Output: true<br>

Example 2:<br>
Input: root = [1,2,2,null,3,null,3]<br>
Output: false<br>
 

Constraints:<br>

The number of nodes in the tree is in the range `[1, 1000]`.<br>
`-100 <= Node.val <= 100`<br>
=======================================================================================<br>
### Evaluate

Assume n represents the number nodes in tree.

- Time Complexity: O(n)
- Space Complexity:
  iterative avarage O(w), w is the maximum width of the tree. Worst case O(n)
  recursive avarage O(h), h is the height of the tree. Worst case O(n)
