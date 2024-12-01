class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Understand:
        input - string, integer and output - integer

        Match:
        string manipulation
        sliding window
        two pointer

        Plan:
        initialize a set with vowels
        initialize a subarray of window size k
        then count the number of variables in the window
        then loop within the string and start at k and end at len(s)
        be adjusting window size as you go and also update count of max vowels in that window size k
        return count

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # Count vowels in the first window
        current_vowels = sum(1 for char in s[:k] if char in vowels)
        max_vowels = current_vowels
        
        # Slide the window
        for i in range(k, len(s)):
            # Remove the first character of previous window
            if s[i-k] in vowels:
                current_vowels -= 1
            
            # Add the new character
            if s[i] in vowels:
                current_vowels += 1
            
            # Update max vowels
            max_vowels = max(max_vowels, current_vowels)
            
            # Early stopping if we've reached the maximum possible
            if max_vowels == k:
                break
        
        return max_vowels



