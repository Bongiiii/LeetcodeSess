class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        Understand:
        input - array of strings, output - array of strings

        Match:
        arrays
        strings
        two pointers

        Plan:
        reverse the entire string, then reverse each word in the string
        create a helper function that reverses the letters, start becomes end
        use the space as a delimeter for swapping
        """
        def reverseHelper(left, right):
            while (left < right):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        #reverse entire array
        reverseHelper(0, len(s) - 1)

        left = 0
        for right in range(len(s)):
            if s[right] == " ":
                reverseHelper(left, right - 1)
                left = right + 1
        
        #reverse the last letters
        reverseHelper(left, len(s)-1)
        