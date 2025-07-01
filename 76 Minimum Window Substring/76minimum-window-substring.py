from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s/c = t/c = O(N)
        countT, window = Counter(t), {}

        res, resLen, l, have, need = [-1,-1], float('inf'), 0, 0, len(countT)

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                #shrink window until have != need
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        #pop left and right pointers of valid min window
        l, r = res

        return s[l:r+1] if resLen != float('inf') else ""