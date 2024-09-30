from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Using the built counter that creates a frequency dictionary
        s/c = t/c = O(N)
        """
        # Use Counter to build the frequency dictionary
        count = Counter(s)
        
        # Find the first unique character
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        
        return -1
