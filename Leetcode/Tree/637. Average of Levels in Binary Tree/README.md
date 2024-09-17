## 637. Average of Levels in Binary Tree
🔗  Link: [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree, BFS, DFS, Binary Tree<br>

=======================================================================================<br>
Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within `10-5` of the actual answer will be accepted.<br>

Example 1:<br>
Input: root = [3,9,20,null,null,15,7]<br>
Output: [3.00000,14.50000,11.00000]<br>
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:<br>
Input: root = [3,9,20,15,7]<br>
Output: [3.00000,14.50000,11.00000]<br>
 

Constraints:<br>

The number of nodes in the tree is in the range `[1, 104]`.<br>
`-231 <= Node.val <= 231` - 1<br>
=======================================================================================<br>
### Evaluate

Where n is the number of nodes in the binary tree.

- Time Complexity: O(n)
- Space Complexity: O(n)
