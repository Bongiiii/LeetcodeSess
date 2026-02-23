class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)

        codeK = 1 << k # Calculate 2^k using bit shift

        # Early termination: if there aren't enough positions to generate all codes
        if n - k + 1 < codeK:
            return False

        # Generate all unique substrings of length k using set comprehension
        uniqSubs = {s[i:i+k] for i in range(n-k+1)}

        # Check if we found all possible binary codes
        return len(uniqSubs) == codeK

        

      