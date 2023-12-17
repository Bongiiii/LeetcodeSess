class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed=0
        while x>0:
            digit = x%10
            reversed = reversed*10 + digit
            x = x// 10
        
        if reversed==original:
            return True
        return False