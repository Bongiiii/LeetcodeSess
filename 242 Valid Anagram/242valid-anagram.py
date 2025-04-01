from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case, differing lengths
        if len(s) != len(t):
            return False

        sDict, tDict = Counter(s), Counter(t)

        return sDict == tDict