from math import sqrt

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # use continuos division by 2 until invalid
        if n <= 0:
            return False

        while n % 2 == 0:
            n//=2

        return n == 1