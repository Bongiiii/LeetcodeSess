class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Understand:
        input - two lowercase strings, output - boolean

        Match:
        string manipulation
        two pointers

        Plan:
        have 2 pointers both starting from the beginning of both strings
        move the pointer on s when the character is found on t else continue traversing t
        loop breaks when pointer on s == len of s


        R/E:
        s/c = O(1), pointer manipulation
        t/c = O(N), n being the max(len(s), len(t))
        """
        i, j = 0, 0

        while (j < len(t) and i < len(s)):
            if s[i] == t[j]:
                i+=1
            j += 1

        return i == len(s)