## 225. Implement Stack using Queues
🔗  Link: [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Stack, Design, Queue<br>

=======================================================================================<br>
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the MyStack class:<br>

`void push(int x)` Pushes element x to the top of the stack.<br>
`int pop()` Removes the element on the top of the stack and returns it.<br>
`int top()` Returns the element on the top of the stack.<br>
`boolean empty()` Returns `true` if the stack is empty, `false` otherwise.<br>

Notes:<br>
You must use only standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.<br>
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.<br>


Example 1:<br>
Input<br>
["MyStack", "push", "push", "top", "pop", "empty"]<br>
[[], [1], [2], [], [], []]<br>
Output<br>
[null, null, null, 2, 2, false]<br>

Explanation<br>
MyStack myStack = new MyStack();<br>
myStack.push(1);<br>
myStack.push(2);<br>
myStack.top(); // return 2<br>
myStack.pop(); // return 2<br>
myStack.empty(); // return False<br>
 

Constraints:<br>

`1 <= x <= 9<br>`
At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.<br>
All the calls to `pop` and `top` are valid.<br>
=======================================================================================<br>
