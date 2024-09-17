## 429. N-ary Tree Level Order Traversal
🔗  Link: [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree, BFS<br>

=======================================================================================<br>
Given an n-ary tree, return the level order traversal of its nodes' values.<br>

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).<br>

Example 1:<br>
Input: root = [1,null,3,2,4,null,5,6]<br>
Output: [[1],[3,2,4],[5,6]]<br>

Example 2:<br>
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]<br>
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]<br>
 

Constraints:<br>

The height of the n-ary tree is less than or equal to `1000`<br>
The total number of nodes is between `[0, 104`]<br>

=======================================================================================<br>
### Evaluate

Where n is the number of nodes in the binary tree.

- Time Complexity: O(n)
- Space Complexity: O(n)
