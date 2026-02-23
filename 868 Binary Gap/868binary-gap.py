class Solution:
    def binaryGap(self, n: int) -> int:
        #bit manipulation
        prev, curr, longest = float('inf'), 0, 0

        while n > 0:
            if n & 1:
                longest = max(longest, curr - prev)
                prev = curr

            curr += 1
            n >>= 1

        return longest

