from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        so create a dict that keeps track of num and freq as key - val pair
        then have a set for keeping track of unique freq
        if unique return true else false
        """
        uniqSet, freqDict = set(), Counter(arr)

        for freq in freqDict.values():
            if freq in uniqSet:
                return False

            uniqSet.add(freq)

        return True
        

        

        