class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        #edge case when length of array is less than k

        #reverse helper func
        def reverseHelper(start,end):
            while end > start:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        #edge case when k > n or wraps around
        k = k % (n+1) 
        
        #reverse whole thing
        reverseHelper(0, n)

        #reverse upto k
        reverseHelper(0, k-1)

        #reverse the rest
        reverseHelper(k, n)
    