## 116. Populating Next Right Pointer in Each Node
🔗  Link: [Populating Next Right Pointer in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree, BFS, DFS, Binary Tree, Linked List<br>

=======================================================================================<br>
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:<br>

struct Node {<br>
  int val;<br>
  Node *left;<br>
  Node *right;<br>
  Node *next;<br>
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.<br>

Initially, all next pointers are set to `NULL`.<br>

Example 1:<br>
Input: root = [1,2,3,4,5,6,7]<br>
Output: [1,#,2,3,#,4,5,6,7,#]<br>
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.<br>

Example 2:<br>
Input: root = []<br>
Output: []<br>
 

Constraints:

The number of nodes in the tree is in the range `[0, 2^12 - 1]`.<br>
`1000 <= Node.val <= 1000<br>`

=======================================================================================<br>
### Evaluate

Where n is the number of nodes in the binary tree.

- Time Complexity: O(n)
- Space Complexity: O(w) for BFS, w is max level size(tree level width); O(log n) for DFS
