class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #pointer to mark the start of traversal, variable for longest substring so far and set to check for duplicates

        left, longest, uniqueChar = 0, 0, set()

        for right in range(len(s)):
            #handle duplicates
            while s[right] in uniqueChar:
                uniqueChar.remove(s[left])
                left += 1

            #unique character
            uniqueChar.add(s[right])
            longest = max(longest, right - left + 1)
    
        return longest