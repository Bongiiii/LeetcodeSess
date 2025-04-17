class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle =  k % (2*(n-1))

        if cycle < n:
            return cycle
        return 2 * (n - 1) - cycle
    