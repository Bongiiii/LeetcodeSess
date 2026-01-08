class Solution:
    def maxDepth(self, s: str) -> int:
        """
        U:
        input - string, output - integer

        given a string of an eqn, return the max number of nested parentheses.
 
        M:
        stack
        pointers

        P:
        iterate through the string using a pointer as long pointer is less than len of string
        when you encounter say an opening parenthesis add to stack
         (since parenthesis is guranteed to be valid so no worry of imbalances) 
        and add count of opening parenthesis/ keep track
        if you encounter a closing parenthesis, pop from stack and decrease count of parenth
         s/c = O(n) size of stack, t/c =O(n) - n len of string

        optimized:
        instead of storing the stack, just use pointers to keep count of max depth
         s/c = O(1), t/c =O(n) - n len of string

        I:
        R:
        E:
        s/c = O(1), t/c =O(n) - n len of string
        """
        max_count, i, stack, curr_count = 0, 0, [], 0

        for character in s:
            if character == "(":
                curr_count += 1
                max_count = max(max_count, curr_count)

            elif character == ")":
                curr_count -= 1

        return max_count
            
                    



