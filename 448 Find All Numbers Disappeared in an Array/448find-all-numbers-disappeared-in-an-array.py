class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #remove duplicates and introduce O(1) lookup
        resSet = set(nums)

        #list comprehension handles searching for missing number in set
        return [x for x in range(1,len(nums)+1) if x not in resSet]