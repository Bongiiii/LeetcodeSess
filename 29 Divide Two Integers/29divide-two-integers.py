class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Understand:

        Plan:
        initiate a count
        then use subtraction 
        if i can subtract divisor from dividend then increment count
        count is incremented as long dividend is greater or equal to divisor
        then for cases where divisor is negative, keep the sign and then turn divisor positive
         and treat it as I described above fot positives
        then when returning the value prepend the sign and return the resultant int

        R/E:
        just subtraction:s/c = O(1), t/c = O(N) 
        subtraction coupled with bit manipulation specifically left shifting: s/c = O(1), O(logN)
        """
        
         # Edge case: overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Optimize using bit shifting
        result = 0
        while dividend >= divisor:
            temp = divisor
            # multiple = 1
            # while dividend >= (temp << 1):
            #     temp <<= 1
            #     multiple <<= 1
            dividend -= temp
            result += 1
        
        # Apply sign
        if negative:
            result = -result
        
        return result