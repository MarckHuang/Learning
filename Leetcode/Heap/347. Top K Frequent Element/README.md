## 347. Top K Frequent Elements
🔗  Link: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hashmap, Heap<br>

=======================================================================================<br>
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.<br>

Example 1:<br>
Input: nums = [1,1,1,2,2,3], k = 2<br>
Output: [1,2]<br>

Example 2:<br>
Input: nums = [1], k = 1<br>
Output: [1]<br>


Constraints:<br>
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range `[1, the number of unique elements in the array]`
- It is guaranteed that the answer is unique
- =======================================================================================<br>
### Evaluate
Assume N represents the number of items in the array `nums`

- Time Complexity: O(N log k) since inserting elements into the heap takes O(log k) time for each of the N elements
- Space Complexity: O(N) for storing the frequency map, and O(k) for the heap, resulting in O(N + k). In the worst case, this can be O(N)
