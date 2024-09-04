## 150. Evaluate Reverse Polish Notation
🔗  Link: [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Stack<br>

=======================================================================================<br>
You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:<br>
Input: tokens = ["2","1","+","3","*"]<br>
Output: 9<br>
Explanation: ((2 + 1) * 3) = 9<br>

Example 2:<br>
Input: tokens = ["4","13","5","/","+"]<br>
Output: 6<br>
Explanation: (4 + (13 / 5)) = 6<br>

Example 3:<br>
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]<br>
Output: 22<br>
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5<br>
= ((10 * (6 / (12 * -11))) + 17) + 5<br>
= ((10 * (6 / -132)) + 17) + 5<br>
= ((10 * 0) + 17) + 5<br>
= (0 + 17) + 5<br>
= 17 + 5<br>
= 22<br>


Constraints:<br>
- 1 <= tokens.length <= 10^4<br>
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]


=======================================================================================<br>
### Evaluate

Assume n be the total number of elements in array tokens.

- Time Complexity: O(n)
- Space Complexity: O(n)
