class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Find min number of consecutive characters instead of
         directly finding substring(s)
        """
        i, n, consecArr = 0, len(s), []

        while i < n:
            count = 1

            while i + 1 < n and s[i+1] == s[i]:
                count += 1
                i += 1

            consecArr.append(count)
            i += 1


        res = 0
        for j in range(1, len(consecArr)):
            res += min(consecArr[j - 1], consecArr[j])

        return res
