class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Understand:
        imput - string, output - boolean

        Match:
        string manipulation
        two pointer

        Plan:
        first preprocess the string by removing space,
         convert to lower case and keep alphanumeric characters only.
        then check if the string is palindrome which is done by comparing
         characters from either extremes, start and end and break
         immediately if they are different.
        update the pointers if the characters are identical by moving
         the pointers in by adding 1 and or subtracting 1 till they cross.
        
        Implement:
        check code below

        Review/Evaluate:
        s/c = t/c =   O(N)
        
        """
        #remove space, reduce to lower cases and take only alphanumeric characters
        procStr = "".join(x for x in s.strip().lower() if x.isalnum())

        #check for palindrome
        left, right = 0, len(procStr) - 1

        while left <= right:
            #early check and exit if characters don't match
            if procStr[left] != procStr[right]:
                return False
            #same characters found, hence update pointers
            left += 1
            right -= 1

        return True

