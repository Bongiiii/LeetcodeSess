class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        n=len(nums)
        #monotonic = True
        #nonmonotonic = False
        i=0

        if nums.sort()!=nums[i:] or nums.sort(reverse=True)!=nums[i:]:
            nonmonotonic = False
        else:
            monotonic = True
        #for i in range(n):
            #elif nums[i]<=nums[i+1] or nums[i]>=nums[i+1]:
                #return True
            
        """

        """
        numsForward = sorted(nums)
        numsBack = numsForward[::-1]

        if nums == numsForward or nums == numsBack:
            return True
        else:
            return False
        """

        numsForward = sorted(nums)
        numsBack = sorted(nums, reverse=True)

        if nums == numsForward or nums == numsBack:
            return True
        else:
            return False




        """

        increasing = decreasing = True

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                decreasing = False
            
            if nums[i] < nums[i - 1]:
                increasing = False

        return increasing or decreasing
        """

            




    
              