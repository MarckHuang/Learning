## 20. Valid Parentheses
🔗  Link: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Stack, String<br>

=======================================================================================<br>
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.<br>

An input string is valid if:<br>

Open brackets must be closed by the same type of brackets.<br>
Open brackets must be closed in the correct order.<br>
Every close bracket has a corresponding open bracket of the same type.<br>

Example 1:<br>
Input: s = "()"<br>
Output: true<br>

Example 2:<br>
Input: s = "()[]{}"<br>
Output: true<br>

Example 3:<br>
Input: s = "(]"<br>
Output: false<br>

Example 4:<br>
Input: s = "([])"<br>
Output: true<br>


Constraints:<br>

`1 <= s.length <= 104`<br>
s consists of parentheses only `'()[]{}'`.<br>
=======================================================================================<br>
### Evaluate
Assume n represents the characters number in the giving string.

- Time Complexity: O(n)
- Space Complexity: O(n)
