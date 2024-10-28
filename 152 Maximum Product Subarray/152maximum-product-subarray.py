class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Understand:
        input - array of integers, output - integer
        Problem summary: find the max product of a contiguous subarray

        Match:
        array
        dp/ kadane's algorithm

        Plan:
        initialize a variable for maxProd to the first element in the array
        have another variable to keep track of the working prod/ currProd
        if the prod reaches < 0 , reset currProd to 1 
        be keeping track of the max prod seen as you go
        when you have completed/ traversed/visited all the elements in the array, return the maxprod

        R/E:
        s/c = O(1), varible usage doesnt use extra space
        t/c = O(N), the length of the array
        """
         # Initialize maxProd to the first element and set minProd and currProd to the same
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]

        # Loop through the elements starting from the second element
        for i in range(1, len(nums)):
            # If the current element is negative, swap maxProd and minProd
            if nums[i] < 0:
                maxProd, minProd = minProd, maxProd

            # Update maxProd and minProd to include the current element
            maxProd = max(nums[i], maxProd * nums[i])
            minProd = min(nums[i], minProd * nums[i])

            # Update the result to hold the maximum product found so far
            result = max(result, maxProd)

        return result