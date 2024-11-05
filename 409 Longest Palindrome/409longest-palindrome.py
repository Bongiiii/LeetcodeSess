from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Understand:
        input - string, output - integer

        Match:
        hashmap

        Plan:
        since this will have lower and uppercase characters, hence I don't need to process for that
        hoping the counter dict also treats lower case and uppercase characters as different
        then check for the freq of each character, if it's even add that number to count variable that counts length
        if it's odd, greater than 2, floor divide by 2 and add quotient to count, if it's less than 2, have a variable that
        keeps track of those and add to it, when you have found all pairs, just add one to the final count when there exists 
        singular characters
        and return the count  

        R/E:
        s/c = O(1), there are only 26 characters in the alphabet
        t/c = O(N), n = length of counter dictionary 

        """
        if len(s) == 1:
            return 1

        stringFreq = Counter(s)

        count, noPair = 0, False

        for freq in stringFreq.values():
            # Add the even portion of the frequency
            count += freq // 2 * 2
            # Check if there's an odd character count
            if freq % 2 == 1:
                noPair = True

        # If there's at least one odd count, we can add one more character to the center
        return count + 1 if noPair else count

        