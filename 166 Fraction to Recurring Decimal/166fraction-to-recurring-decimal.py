class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        Understand:
        input - 2 integers, output - string
        Problem summary: Given two integers, numerator and denominator,compute the decimal fraction and return it.

        Match:
        Math

        Plan:
        just using the division formula which is num/denom
        we care about the decimal digits hence the / instead of //
        so have a variable called decimal that tracks the fraction
        instead of immediately type casting to a string and returning
        check if length is greater than 10^4, if so then check if there are repeating values, if so enclose that section in parentheses
        else just type cast to a string

        R/E:
        s/c = O(N), variable usage
        t/c = O(N)
        """
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values for ease
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Append the integer part
        result.append(str(numerator // denominator))
        
        # Calculate the remainder
        remainder = numerator % denominator
        
        # If there is no remainder, return the integer part
        if remainder == 0:
            return ''.join(result)
        
        # Otherwise, handle the fractional part
        result.append(".")
        remainder_map = {}
        
        while remainder != 0:
            # If the remainder is already seen, we found the repeating part
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            
            # Store the remainder and its position in the result
            remainder_map[remainder] = len(result)
            
            # Multiply remainder by 10 and find the next digit
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(result)