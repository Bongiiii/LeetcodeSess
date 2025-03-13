class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Understand:
        input - array of integers, output - integer

        Match:
        dp - O(N^2) time
        array manipulation
        greedy algorithm

        Plan:
        have a variable that keeps track of the number of jumps that can be taken, and 
        a variable assigned the lastindex
        make use of the enumerate so as to be able to access the indices and the elements simultaneously

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        
        countJump, maxDist, lastReach = 0, 0, 0
        #base case, one element
        if len(nums) == 1:
            return 0

        for idx, num in enumerate(nums[:-1]):
        
            maxDist = max(maxDist, num + idx)

            if lastReach == idx:
                countJump += 1
                lastReach = maxDist

        return countJump

                