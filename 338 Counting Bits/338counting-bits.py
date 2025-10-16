class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Understand:
        find and return count of 1s in the integer's bits rep

        Match:
        bit manipulation
        dynamic programming

        Plan:
        initialize an array to store count of 1s, have a variable that
         counts 1s in an integer 
        return the array

        Implement:

        R/E:

        """
        #using built in bit_count() func
        return [i.bit_count() for i in range(n+1)]