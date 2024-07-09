class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        count = 0
        
        for i in s:
            if i == '(':
                if count > 0:
                    stack.append(i)
                count += 1
            elif i == ')':
                count -= 1
                if count > 0:
                    stack.append(i)
                
        return ''.join(stack)
            