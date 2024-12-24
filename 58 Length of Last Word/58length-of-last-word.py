class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        solve the problem more efficiently by avoiding the creation of an array. 
        Instead, we can traverse the string in reverse, skipping trailing spaces, and count the characters of the last word.
        """
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length