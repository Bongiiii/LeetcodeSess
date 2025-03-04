class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Understand:
        input - two strings, output - array of integers

        Match:
        two pointers
        sliding window

        Plan:
        have a pointer that keeps the length of the sliding window, length of p
        then have a set that keeps the indices of the anagram characters seen in that window
        when the length of set is equal to the length of p and all anagrams found, append the 
        smallest index in set to the output array, continue until there are no characters to 
        check for anagrams in

        R/E:
        s/c = O(N)
        t/c = O(N)
        """
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)  # Frequency map of 'p'
        s_count = Counter(s[:len(p) - 1])  # Frequency map of first (len(p) - 1) chars in 's'
        
        res = []
        left = 0
        
        for right in range(len(p) - 1, len(s)):
            s_count[s[right]] += 1  # Include new character in window
            
            if s_count == p_count:  # Check if current window matches
                res.append(left)
            
            s_count[s[left]] -= 1  # Remove leftmost character from window
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1  # Slide window forward
        
        return res


                
