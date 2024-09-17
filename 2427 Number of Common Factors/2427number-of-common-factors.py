class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """
        Understand:
        input: two integers, output: integer
        problem summary: given two integers, count the number of common factors between them

        Match:
        math, factorization

        Plan:
        initialize a variable to store count of common factors
        iterate from 1, upto the smallest input integer(inclusive so + 1)
        then check if that value is a factor of a and b, then increment count
        else continue

        R/E:
        s/c = O(1), just variable assignments
        t/c = O(N), n being min(a,b)

        """
        count, minInt = 0, min(a, b)

        for factor in range(1, minInt + 1):
            if (a % factor == 0) and (b % factor == 0):
                count += 1
            
        return count