## 1047. Remove All Adjacent Duplicates in String
🔗  Link: [Remove All Adjacent Duplicates in String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: String, Stack<br>
=======================================================================================<br>
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:<br>
Input: s = "abbaca"<br>
Output: "ca"<br>
Explanation: <br>
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".<br>

Example 2:<br>
Input: s = "azxxzy"<br>
Output: "ay"<br>
 
Constraints:<br>

`1 <= s.length <= 105<br>`
`s` consists of lowercase English letters.<br>
=======================================================================================<br>
### Evaluate
Assume n is the length of the input string.<br>

- Time Complexity: O(n)<br>
- Space Complexity: O(n)<br>
