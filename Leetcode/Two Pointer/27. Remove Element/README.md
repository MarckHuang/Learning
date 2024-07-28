## 27. Remove Element
🔗  Link: [Remove Element](https://leetcode.com/problems/remove-element/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: two pointer<br>

=======================================================================================<br>

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.<br>

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:<br>

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.<br>
- Return `k`.

Example 1:<br>
Input: nums = [3,2,2,3], val = 3<br>
Output: 2, nums = [2,2, _, _]<br>

Example 2:<br>
Input: nums = [0,1,2,2,3,0,4,2], val = 2<br>
Output: 5, nums = [0,1,4,0,3, _, _, _]<br>
 
Constraints:<br>
- 0 <= nums.length <= 100<br>
- 0 <= nums[i] <= 50<br>
- 0 <= val <= 100<br>

=======================================================================================<br>

## Evalute
Assume n be the total number of operations performed.

- Time Complexity: O(n)
- Space Complexity: O(1)
