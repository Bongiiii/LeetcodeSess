class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Understand:
        input - string, output - integer
        problem summary: given a string, return the number of palindromic substrings you can create

        Match:
        string manipulation

        Plan:
        the problem seems to cater for duplicates
        every char in string can be it's own palindrome separately
        then initiate a count to the length of strings
        check for palindromes using the two pointer technique
        delete/omit characters if they are not palindromes
        else continue checking for the rest of the portions
        return count

        R/E:
        s/c = O(n), recursive calls to the helper function
        t/c = O(N^2)
        """
        
        # Helper function to expand around center and count palindromes
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            # Expand while the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        count = 0
        # Loop through each character in the string
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            count += expand_around_center(i, i)
            # Even length palindromes (two characters center)
            count += expand_around_center(i, i + 1)
        
        return count
        