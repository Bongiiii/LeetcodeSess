class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        """
        Understand:
        input - string, output - integer
        prob summary: given a string, return the number of substrings that contains vowels

        Match:
        string manipulation
        sliding window
        
        Plan:
        intuition - scan the string starting from both ends, while checking for vowels
         and then shrink either left, and right until your reach the middle(pointers, coincide) and return count
        have a helper function that checks for vowels in a window
        then shrink left
        shrink right
        have a set or dictionary that keeps the vowels for reference(won't eat up space as vowels are always 5, sos/c = O(1))

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        vowels, n = set("aeiou"), len(word)

        return sum(set(word[i:j])==vowels for i in range(n) for j in range(i + 1, n + 1) )
        