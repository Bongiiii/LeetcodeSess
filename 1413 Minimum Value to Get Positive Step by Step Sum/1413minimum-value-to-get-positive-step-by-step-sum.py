class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Input: array of integers, output: integer

        Match:
        math
        array manipulation
        two pointer

        Plan:
        have a pointer that starts at the beginning and holds as the curr num to be added to
        then have a loop that enumerates through the array, and use it to add to the curr
        once curr goes below 0, reset curr by moving the pointer that assigns value to curr
        also have a conditional that takes even -ve nums as curr and checks if by adding
         it doesnt go down further
        return the max sum seen so far, that means i need a variable for that and I also
         need to be updating it

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        cumulative_sum = 0
        min_cumulative_sum = 0
        
        for num in nums:
            cumulative_sum += num
            min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)
            
        # To ensure the minimum cumulative sum is >= 1, we need startValue at least -min_cumulative_sum + 1
        startValue = -min_cumulative_sum + 1
        return startValue