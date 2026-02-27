# 1. Two Sum

**Difficulty:** Easy  
**Topics:** Array, Hash Table  
**Link:** [LeetCode Problem](https://leetcode.com/problems/two-sum/)  
**Date Solved:** 2024-01-01 (Example)

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Approach

### Initial Thoughts
- The brute force approach would be to check every pair of numbers
- This would require nested loops - O(n²) time complexity
- We can optimize using a hash table to store complements

### Solution Strategy
1. Create a hash map to store numbers we've seen and their indices
2. For each number, calculate its complement (target - current number)
3. Check if the complement exists in our hash map
4. If found, return the current index and the complement's index
5. If not found, add the current number and its index to the hash map

### Time Complexity
- O(n) - We traverse the list once

### Space Complexity
- O(n) - In the worst case, we store all elements in the hash map

## Solution Code

```python
# Language: Python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number and its index
        seen = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if complement exists in our dictionary
            if complement in seen:
                return [seen[complement], i]
            
            # Store the current number and its index
            seen[num] = i
        
        # No solution found (though problem guarantees one exists)
        return []
```

## Alternative Approaches

### Approach 2: Brute Force
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Trade-offs:** Simpler to understand but much slower for large inputs

## Test Cases

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6

Input: nums = [3,3], target = 6
Output: [0,1]
Explanation: nums[0] + nums[1] = 3 + 3 = 6
```

## Lessons Learned

- Hash tables are excellent for O(1) lookup time problems
- The complement pattern (target - current) is common in array problems
- Always consider the trade-off between time and space complexity
- One-pass hash table approach is more efficient than sorting + two pointers for this specific problem

## Related Problems

- [15. 3Sum](https://leetcode.com/problems/3sum/)
- [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)

## Tags
`array` `hash-table` `easy`
