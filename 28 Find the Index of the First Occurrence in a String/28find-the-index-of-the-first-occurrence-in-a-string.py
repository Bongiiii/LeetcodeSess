class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Step 1: Create the LPS array
        def computeLPSArray(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0  # length of the previous longest prefix suffix
            i = 1
            
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            
            return lps
        
        # Step 2: KMP Search
        m = len(needle)
        n = len(haystack)
        
        lps = computeLPSArray(needle)
        i = 0  # index for haystack
        j = 0  # index for needle
        
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            
            if j == m:
                return i - j  # match found, return the start index
            
            elif i < n and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1  # no match found
