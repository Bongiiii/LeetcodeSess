class Solution:
    def myAtoi(self, s: str) -> int:
        #skip white space
        i, n, intMax, intMin = 0, len(s), (2**31)-1, (-2**31)
        
        while (i < n) and s[i] == " ":
            i += 1
        
        if i == n:
            return 0
        #fix sign
        sign = -1 if s[i] == "-" else 1
        if s[i] in ["-", "+"]:
            i += 1
            
        #find digits
        num = 0
        while (i<n) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
            
        #apply sign to num
        num*=sign
        
        if num < intMin:
            return intMin
            
        elif num > intMax:
            return intMax
        else:
            return num