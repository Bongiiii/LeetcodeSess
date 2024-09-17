class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Understand:
        input: integer, output: boolean
        problem summary: given a number, determine if the 
        factors of the number are limited to 2, 3, and 5. 
        If so, return True, else False.

        Match:
        This problem is about factorization. We need to repeatedly divide the number 
        by 2, 3, and 5 until it is no longer divisible by these numbers. 
        This is a straightforward division problem with a loop.

        Plan:
        - Check if the number is greater than 0, because non-positive numbers cannot 
          be ugly.
        - Repeatedly divide the number by 2, 3, and 5 if it is divisible by these 
          factors.
        - After dividing, if the number is reduced to 1, return True because it means 
          the number is composed only of the factors 2, 3, and 5.
        - Otherwise, return False.

        R/E (Review/Explain):
        Space Complexity (s/c): O(1) because we only use a few variables.
        Time Complexity (t/c): O(log n) because we're repeatedly dividing the number, 
        reducing it by a factor of 2, 3, or 5.
        """

        # Base case: numbers less than or equal to 0 are not ugly
        if n <= 0:
            return False

        # 1 is always an ugly number
        if n == 1:
            return True
            
        # Divide n by 2, 3, or 5 as long as it is divisible
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        
        # If after all divisions, n becomes 1, it is an ugly number
        return n == 1
