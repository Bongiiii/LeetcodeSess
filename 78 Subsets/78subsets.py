class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Understand:
        input - array of integers, output = array of arrays of integers
        powerset result should have 2^n(number of elements in array or len of array)

        Match:
        math
        array manipulation
        backtracking

        Plan:
        initialize an array to store resultant array, let it have an empty array in it already
        have a helper function that uses backtracking to create subsets of the array elements


        R/E:
        s/c = t/c = O(N)
        """
        res = []
        
        def backtrackHelper(start, path):
            if start == len(nums):
                res.append(path)
                return

            backtrackHelper(start + 1, path + [nums[start]])
            backtrackHelper(start + 1, path)

        # Start backtracking with an empty subset
        backtrackHelper(0, [])
        return res