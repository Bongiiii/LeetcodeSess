class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Understand:
        input - array of strings, output - integer
        edge case: no digits, or just weird characters

        Match:
        Math
        array manipulation

        Plan:
        use a stack to store numbers as you iterate the array
        when you encounter an operator, pop 2 elements from the stack and use them as operands for the operator 
        append the result to the stack 
        when finished, the stack should have only one number

        R/E:
        s/c = O(N)
        t/c = O(N)
        """

        stack = []

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                #append number to stack and convert to int
                stack.append(int(token))

            #when it's not a digit and is an operator:
            else:
                if token == "+":
                    # Pop the last two numbers, add them, and push the result back
                    stack[-2] += stack[-1]
                elif token == "-":
                    # Pop the last two numbers, subtract the second from the first, and push back
                    stack[-2] -= stack[-1]
                elif token == "*":
                    # Pop the last two numbers, multiply, and push the result back
                    stack[-2] *= stack[-1]
                else: # Division
                    # Ensure integer division for negative numbers too
                    stack[-2] = int(float(stack[-2]) / stack[-1])
                # Pop the last number (second operand) from the stack as it's been used
                stack.pop()

        return stack[0]