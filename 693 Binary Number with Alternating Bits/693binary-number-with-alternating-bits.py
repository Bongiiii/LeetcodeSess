class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Bruteforce:
        - convert from base 10 to 2, by dividing with 2
        - then keep remainder in array and iterate through array and check 

        s/c = t/c = len of binary array
        
        OptimaL USINg bit manipulation
        """
        prevBit = -1

        while n > 0:
            currBit = n & 1

            if prevBit == currBit:
                return False

            prevBit = currBit
            #shift to new curr

            n >>= 1

        return True