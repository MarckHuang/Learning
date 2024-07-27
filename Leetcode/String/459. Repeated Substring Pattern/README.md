## 459. Repeated Substring Pattern
🔗  Link: [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: String, Prefix<br>

=======================================================================================<br>

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:<br>
Input: s = "abab"<br>
Output: true<br>
Explanation: It is the substring "ab" twice.<br>

Example 2:<br>
Input: s = "aba"<br>
Output: false<br>

Example 3:<br>
Input: s = "abcabcabcabc"<br>
Output: true<br>
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.<br>
 
Constraints:<br>
1 <= s.length <= 104
s consists of lowercase English letters.

=======================================================================================<br>
### Evaluate

Assume n is the length of the string s.

Time Complexity: O(n)
Space Complexity: O(n)
