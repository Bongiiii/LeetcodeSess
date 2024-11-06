class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Understand:
        input - array of integers, output - integer

        Match:
        Boyer Moore voting algorithm

        Plan:
        iterate through the array and have variables to keep track of count of the characters
        have a variable to also track the major element seen so far

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        count, majElem = 0, 0

        for num in nums:
            if count == 0:
                majElem = num

            if num != majElem:
                count -= 1
            
            else:
                count += 1

        return majElem