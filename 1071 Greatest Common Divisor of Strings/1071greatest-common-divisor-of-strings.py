from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        UUnderstand:
        input - 2 strings, output - string

        Match:
        two pointer
        string manipulation
        hashset

        Plan:
        
        R/E:
        s/c = O(1)
        t/c = O(len(str1)+len(str2)),
        """
        # Check if str1 and str2 have a common pattern
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of str1 from 0 to gcd_length
        return str1[:gcd_length]