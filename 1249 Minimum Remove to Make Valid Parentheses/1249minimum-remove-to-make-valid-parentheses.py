class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        output = list(s)

        # Iterate through the characters of the input string
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    output[i] = ''

        # Remove any remaining opening parentheses from the output string
        while stack:
            output[stack.pop()] = ''

        # Convert the output list to a string and return
        return ''.join(output)


