class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        U:
        input - string, an integer variable

        given a string, crush/delete when string has k identical characters adjacent

        M:
        stack
        pointer/sliding window

        P:
        iterate string using pointers
        when you encouter consecutive identical characters
         modulo divide by k and pop stack when result is 0,
         else add that character and count to stack
         then add the resultant stack after removing identical adjacent characters
         and return resultant string

        I:
        R:
        s/c = O(n), n number of characters in string in worst case where you can crush anything
        t/c = O(n), n - length of string as we visit every character
        E:
        """
        stack = []  
        
        for i in range(len(s)):
            if not stack:
                stack.append([s[i], 1])
            else:
                if stack[-1][0] == s[i]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop() 
                else:
                    stack.append([s[i], 1])
        
        return "".join(char * count for char, count in stack)
            