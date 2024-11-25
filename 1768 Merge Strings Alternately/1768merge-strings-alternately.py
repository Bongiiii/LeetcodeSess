class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Understand:
        input - 2 strings, output - string

        Match:
        two pointer, string

        Plan:
        iterate both strings for the length of the min string
        then add alternatively, starting with word1, followed by word2
        when there are remaining characters in the string, just append them

        R/E:
        s/c = O(n+m), n = word1, m = word2
        t/c = O(max(word1, word2))
        """
        n, i, output = min(len(word1), len(word2)), 0, ""
        
        while(i<n):
            output += word1[i]
            output += word2[i]
            i += 1

        # Append remaining characters
        if len(word1) > len(word2):
            output += word1[i:]  # Add the rest of word1
        else:
            output += word2[i:]  # Add the rest of word2

        return output

