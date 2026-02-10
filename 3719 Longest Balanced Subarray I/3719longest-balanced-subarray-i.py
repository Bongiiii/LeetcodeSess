class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        """
        U:
        input - integer array, output - integer

        Bruteforce:
        have a set to make sure we have distinct characters
        iterate through array and check parity of numbers and
         be adding to set if integer is distinct
        have 2 counter variables to keep track of odd and even numbers count
        if len of odd and even match then return len of orig array else
         return the sum of odd and even count

        s/c = O(s), size of set...number of distinct characters
        t/c = O(n), visiting every element in array
        """
        n = len(nums)
        max_length = 0
        
        # Try every possible starting point
        for start in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            # Expand the subarray from 'start' to the end of the list
            for end in range(start, n):
                num = nums[end]
                
                # Update our sets for the current subarray [start...end]
                if num % 2 == 0:
                    distinct_evens.add(num)
                else:
                    distinct_odds.add(num)
                
                # Check if the current subarray is balanced
                if len(distinct_evens) == len(distinct_odds):
                    # If balanced, update the max_length found so far
                    # The length is (end - start + 1)
                    current_length = end - start + 1
                    if current_length > max_length:
                        max_length = current_length
                        
        return max_length