class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Understand:
        input: array of even length, output:integer representing max sum pair

        problem summary: given an even kength array, return the min max pair sum array

        Match:
        two pointers
        tuples
        array of arrays
        sliding window

        Plan:
        sort the array
        pair up numbers in such a way left(smallest) and right(largest)
        use the two pointers to traverse nums and do the pairing
        continue until left > right
        have a variable to track and update the max

        """
        nums.sort()
        left, right = 0, len(nums) - 1
        minMaxSum = float("-inf")
        
        while (left < right):
            minMaxSum = max(minMaxSum, nums[left] + nums[right])
            left += 1
            right -= 1

        return minMaxSum
