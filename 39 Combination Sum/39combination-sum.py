class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Understand:
        input - array of integers, integer, output - array of arrays

        Match:
        array manipulation
        math
        hashmap

        Plan:
        iterate through array and be checking if we can divide the target with each num
        then check if there's a difference in array

        R/E:
        s/c =  O(N), from recursive calls
        t/c = O(2^T)
        """
        output = []

        #helper function to find combinations
        def backtrack(nums, start, remaining, combo):
            if remaining == 0:
                output.append(combo[:])
                return

            for i in range(start, len(nums)):
                num = nums[i]
                if remaining - num < 0:
                    continue
                backtrack(nums, i, remaining - num, combo + [num])


        
        backtrack(candidates, 0, target, [])
        return output