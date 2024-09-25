class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Understand:
        input - non-negative integer, output - integer
        problem summary: given a positive integer, find its square root without using built-in functions.

        Match:
        math
        binary search
        integer approximation

        Plan:
        The square root of x is less than or equal to half of x for x >= 4.
        Use binary search to narrow down the square root between 0 and x.
        Return the largest integer such that i * i <= x.

        R/E:
        s/c = O(1)
        t/c = O(log N), using binary search to optimize time.
        """
        if x < 2:  # Base case for x = 0 and x = 1
            return x
        
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid  # Exact square root found
            elif square < x:
                left = mid + 1  # Look for larger values
            else:
                right = mid - 1  # Look for smaller values
        
        return right  # Return the integer part of the sqrt


        