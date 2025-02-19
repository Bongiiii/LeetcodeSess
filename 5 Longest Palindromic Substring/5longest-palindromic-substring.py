class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Understand:
        input - string, output - string

        Match:
        center expansion
        dp
        string manipulation

        Plan:
        initialize a 2d array to store booleans whether the characters in the string make up palindromes or not


        R/E:
        s/c = t/c = O(N^2)
        """
        n = len(s)  # Length of the string
      
        mx_len = 1
        start = 0

        def expandFromCenter(s, n, l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
            
        for i in range(n):
            # Odd Length Palindromes
            odd_len = expandFromCenter(s, n, i, i)
            if odd_len > mx_len:
                mx_len = odd_len
                start = i - mx_len // 2
        
            # Even Length Palindromes
            even_len = expandFromCenter(s, n, i, i + 1)
            if even_len > mx_len:
                mx_len = even_len
                start = i - (mx_len - 1) // 2
      
        # Return the longest palindrome substring
        return s[start : start + mx_len]