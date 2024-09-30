class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Understand:
        input - array of strings, output - string
        problem summary: given an array of strings, find the longest common prefix

        Match:
        string/ array manipulation

        Plan:
        initiate a key/map for the first element
        iterate through array from 0 to len(strs)
        check each character in the first word against the rest of the array
        if all characters match, add them to the output string
        """
        # Take the first string as the reference
        key = strs[0]
        res = []

        # Iterate through characters in the first string
        for i in range(len(key)):
            char = key[i]
            # Check if this character is present in the same position of all strings
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return ''.join(res)  # Return the current result if there's a mismatch
            res.append(char)  # Append matching character to result

        return ''.join(res)  # Convert list to string and return
