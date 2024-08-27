class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Understand:
        Given an array of integers, find the length of the longest consecutive sequence.
        
        Plan:
        1. Convert the array to a set for O(1) average-time complexity for lookups.
        2. Iterate through the set, and for each number, check if it's the start of a sequence.
        3. Use a while loop to find the length of the sequence.
        
        Time Complexity: O(N)
        Space Complexity: O(N) due to the space used by the set.
        """
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if `num` is the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1
                
                max_length = max(max_length, length)
        
        return max_length
