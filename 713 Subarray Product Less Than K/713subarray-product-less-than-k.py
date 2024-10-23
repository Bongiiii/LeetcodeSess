class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Understand:
        input - array of integers and an integer, output - integer
        problem summary: Given an array of integers, and an integer, return the length of the subarrays that the elements product is less than the integer

        Match:
        math
        array manipulation
        two pointers
        sliding window

        Plan:
        have a variable to keep count of subarrays we can make using the elements in the array
        also I don't want to explicity create the subarrays, just use the variables and manipulate the currect array in place
        i will initiate the count variable to the number of elemnts in the array as all elements of the array are also subsets
        then have a sweep, using two pointers
        one pointer at the start of the array and the other a pointer ahead
        then to update the pointers, first check if multiplying

        R/E:
        s/c = O(1)
        t/c = O(N)

        """
        #base case
        # if k == 0:
        #     return 0

        subArrayCount, i, prod = 0, 0, 1
        #first sweep checking if element is a subarray
        # for num in nums:
        #     if num < k:
        #         subArrayCount += 1

        #subarrays with variable windows
        for j in range(len(nums)):
            prod *= nums[j]

            while prod >= k and i <= j:
                prod //= nums[i]
                i += 1

            subArrayCount += (j - i + 1)
        return subArrayCount
                





