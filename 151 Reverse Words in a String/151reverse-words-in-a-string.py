class Solution:
    def reverseWords(self, s: str) -> str:
        """
        start from the end and grab words and add to array, 
        then when done join words into string using string with
         single space between words 
        """
        end,res = len(s), []
        i = end - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break

            # Find the start of the word
            word_end = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            #found a space " " signaling you have found a word
            word_start = i + 1

            # Add the word to the result list
            res.append(s[word_start:word_end + 1])

        # Join the words with a single space
        return ' '.join(res)



        