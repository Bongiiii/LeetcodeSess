class Solution:
    def decodeString(self, s: str) -> str:
        """
        U:
        input - string, output - string

        M:
        stack 
        string manipulation
        pointers

        P:
        iterate through the string, character by character
        handle the digits and store them in a stack and also store characters in a string,
         triggered by and opening parentheses, push to stack and reset
        when you encounter a closing a closing parentheses build result and pop from stack
        when you encounter a regular character continue building substring/repetition

        I:
        R:
        s/c = O(n+m), n length of string, and m is max number length of decoded string
        t/c = O(n*m)
        E:
        """
        num, res, count_stack, substring_stack = 0, '', [], []
        for c in s:
            #handle digits
            if c.isdigit():
                num = num * 10 + int(c)

            #handle when you encounter opening parenthesis
            elif c == "[":
                count_stack.append(num)
                substring_stack.append(res)
                res = ''
                num = 0

            #closing parenthesis case
            elif c == "]":
                res = substring_stack.pop() + res * count_stack.pop()

            # building substring 
            else:
                res += c

        return res
