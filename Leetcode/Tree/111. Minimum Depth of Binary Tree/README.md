## 111. Minimum Depth of Binary Tree
🔗  Link: [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree, Binary Tree, BFS, DFS<br>

=======================================================================================<br>
Given a binary tree, find its minimum depth.<br>

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.<br>

Note: A leaf is a node with no children.<br>

Example 1:<br>
Input: root = [3,9,20,null,null,15,7]<br>
Output: 2<br>

Example 2:<br>
Input: root = [2,null,3,null,4,null,5,null,6]<br>
Output: 5<br>
 

Constraints:<br>

The number of nodes in the tree is in the range `[0, 10^5]`.<br>
`-1000 <= Node.val <= 1000<br>`
=======================================================================================<br>
### Evaluate

Assume n represents the number nodes in tree.

- Time Complexity: O(n)
- Space Complexity:
  BFS O(w), w is maximum width of the tree.
  DFS O(n) for worst case, other O(log n) or O(h), h is the height of the tree
