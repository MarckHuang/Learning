## 239. Sliding Window Maximum
🔗  Link: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Array, Queue, Sliding window, Heap, Monotonic Queue<br>

=======================================================================================<br>
ou are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.<br>

Return the max sliding window.<br>

 

Example 1:<br>
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3<br>
Output: [3,3,5,5,6,7]<br>
Explanation: <br>
Window position                Max<br>
---------------               -----<br>
[1  3  -1] -3  5  3  6  7       3<br>
 1 [3  -1  -3] 5  3  6  7       3<br>
 1  3 [-1  -3  5] 3  6  7       5<br>
 1  3  -1 [-3  5  3] 6  7       5<br>
 1  3  -1  -3 [5  3  6] 7       6<br>
 1  3  -1  -3  5 [3  6  7]      7<br>
 
Example 2:<br>
Input: nums = [1], k = 1<br>
Output: [1]<br>
 

Constraints:<br>

`1 <= nums.length <= 105`<br>
`-104 <= nums[i] <= 104`<br>
`1 <= k <= nums.length`<br>

=======================================================================================<br>
### Evaluate

Assume n is given arrayy lens, and k in size of sliding window.<br>

- Time Complexity: O(n)<br>
- Space Complexity: O(k)<br>
