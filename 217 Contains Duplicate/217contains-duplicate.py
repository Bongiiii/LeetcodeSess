from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    #put array in a dict that keeps track of count of each character, key - number and val - frequency
        freqDict = Counter(nums)

        #iterate through the array
        for num in nums:
            #check freq of num, if > 1 return True
            if freqDict[num] > 1:
                return True

            #else continue checking the rest of the array
            continue

        return False
        