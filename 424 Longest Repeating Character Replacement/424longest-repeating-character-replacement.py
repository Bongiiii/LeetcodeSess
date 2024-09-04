class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Understand:
        input - string, output: integer
        prob summary: given a string, find the longest repeating character with replacement

        Match:
        sliding window
        2pointers

        Plan:
        use sliding window, if longest subtring is requiring more than k replacements, shift window
        """
         # Dictionary to keep track of the frequency of characters in the window
        char_count = {}
        max_count = 0  # To track the count of the most frequent character in the window
        maxLength = 0
        left = 0
        
        for right in range(len(s)):
            # Update the frequency of the character at the right pointer
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            # Update max_count with the maximum frequency in the current window
            max_count = max(max_count, char_count[s[right]])
            
            # Check if the current window is valid
            if (right - left + 1) - max_count > k:
                # If not, shrink the window from the left
                char_count[s[left]] -= 1
                left += 1
            
            # Update maxLength for the longest valid window
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength