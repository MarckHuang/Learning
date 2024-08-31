## 232. Implement Queue using Stacks
🔗  Link: [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Stack, Design, Queue<br>

=======================================================================================<br>
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:<br>

`void push(int x)` Pushes element x to the back of the queue.<br>
`int pop()` Removes the element from the front of the queue and returns it.<br>
`int peek()` Returns the element at the front of the queue.<br>
`boolean empty()` Returns `true` if the queue is empty, `alse` otherwise.<br>

Example 1:<br>
Input<br>
["MyQueue", "push", "push", "peek", "pop", "empty"]<br>
[[], [1], [2], [], [], []]<br>
Output<br>
[null, null, null, 1, 1, false]<br>

Explanation<br>
MyQueue myQueue = new MyQueue();<br>
myQueue.push(1); // queue is: [1]<br>
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)<br>
myQueue.peek(); // return 1<br>
myQueue.pop(); // return 1, queue is [2]<br>
myQueue.empty(); // return false<br>
 

Constraints:<br>`
`1 <= x <= 9<br>
At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.<br>
All the calls to `pop` and `peek` are valid.<br>

=======================================================================================<br>
### Evaluate
Assume n be the total number of elements input.

- Time Complexity: O(n)
