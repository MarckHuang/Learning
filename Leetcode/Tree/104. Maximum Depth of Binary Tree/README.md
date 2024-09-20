## 104. Maximum Depth of Binary Tree
🔗  Link: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree, Binary Tree,BDS, DFS<br>

=======================================================================================<br>
Given the `root` of a binary tree, return its maximum depth.<br>

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.<br>

Example 1:<br>
Input: root = [3,9,20,null,null,15,7]<br>
Output: 3<br>

Example 2:<br>
Input: root = [1,null,2]<br>
Output: 2<br>
 

Constraints:<br>

The number of nodes in the tree is in the range `[0, 10^4]`<br>
`-100` <= Node.val <= `100`<br>
=======================================================================================<br>
### Evaluate

Assume n represents the number nodes in tree.

- Time Complexity: O(n)
- Space Complexity: BFS O(w), w is maximum tree width ; DFS O(h), h is tree height.
