class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Understand:
        input - two strings, output - boolean

        Match:
        string manipulation
        two pointers

        Plan:
        iterate the strings backwards
        when you encounter the '#' skip the next character
        be checking if characters are the same,
        else instantly return false
        finally return true when there is no early return
        
        R/E:
        s/c = O(1), used pointers
        t/c = O(n+m), resultant arrays length...worst case when they are not equal length
        """
        i, j = len(s) - 1, len(t) - 1

        def get_next_valid_index(string, index):
            backspaces = 0
            while index >= 0:
                if string[index] == '#':
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    return index  # Valid character found
                index -= 1
            return index  # Exhausted string
        
        while i >= 0 or j >= 0:
            i = get_next_valid_index(s, i)
            j = get_next_valid_index(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:  # If characters don't match, return False
                    return False

            if (i >= 0) != (j >= 0):  # One string is exhausted before the other
                return False

            i -= 1
            j -= 1

        return True