class Solution:
    def reverse(self, x: int) -> int:
        """
        Understand:
        input: integer, output: reversed integer

        Match:
        Math

        Plan:
        1. Handle negative numbers.
        2. Reverse the digits using modulus and division.
        3. Return 0 if the reversed number overflows 32-bit signed integer range.

        R/E:
        t/c = O(logx)
        s/c =O(1)
        """
        # Define the 32-bit integer boundaries
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Extract the sign of the number
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        result = 0
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        # Restore the sign and check for overflow
        result *= sign
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result
