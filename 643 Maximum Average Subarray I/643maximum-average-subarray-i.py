class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        slid_window = sum(nums[:k])
        maxAvg = slid_window
            
        for i in range(k, len(nums)):
            #remove first element and add new element...update window in short
            slid_window += nums[i] - nums[i-k] 
            maxAvg = max(maxAvg, slid_window)

        return maxAvg/k