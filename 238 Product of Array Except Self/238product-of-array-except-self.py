class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the output array
        output = [1] * n
        
        # Calculate the left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        # Calculate the right products and update the output array
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
