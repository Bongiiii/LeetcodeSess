class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Understand:
        input - strings, output - string
        given two strings, return a string that is the sum of the input strings
        Edge Case Considerations: strings of different lengths, a final carry, and cases like "0" + "0". 
        
        Match:
        binary
        math
        string manipulation

        Plan:
        first type cast the strings into integers
        remember we are used to base 10 addition, but this is base 2, use the same principles, when you get 2(binary only has 1 and 0s)
         just carry a remainder and put 0
        then have a variable to store the sum, and a variable for the remainder
        addition starts from right to left, inorder to avoid that reverse input strings
        so use two pointers to traverse the input strings
        and then store the values in a string
        when you have added all the values, return the reverse of the sum string

        R/E:
        s/c = O(max(N,M)), n length of output string
        t/c = O(max(N,M)), n - length of string a and m - length of string b
        """
         # Reverse input strings to process from least to most significant digit
        a, b = a[::-1], b[::-1]

        # Variables to store the sum and the carry
        sumString = ""
        carry = 0

        # Process each digit up to the longest input length
        max_length = max(len(a), len(b))
        for i in range(max_length):
            # Get binary digits from a and b or use 0 if index is out of bounds
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            
            # Calculate sum for this digit plus any carry
            total = digit_a + digit_b + carry
            
            # Append the current binary digit to the result (0 or 1)
            sumString += str(total % 2)
            
            # Update the carry
            carry = total // 2

        # Append any remaining carry
        if carry:
            sumString += "1"

        # Reverse the result to get the final binary sum
        return sumString[::-1]

