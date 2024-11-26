class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Understand:
        input - string, output - string

        Constraints:
        Edge case: Cannot have an empty string (string length starts at least 1).

        Match:
        String manipulation with two pointers.

        Plan:
        - Convert string into a mutable array since strings are immutable.
        - Use a set of vowels for quick lookup (both uppercase and lowercase).
        - Use two pointers, starting at opposite ends.
        - Swap vowels when found, and continue until pointers cross.
        - Return the resultant string.

        R/E:
        Space complexity: O(1), as the set of vowels is constant size.
        Time complexity: O(N), where N is the length of the string.
        """
        vowels, i, j = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}, 0, len(s) - 1
        string = list(s)  # Convert string to mutable list

        while i < j:
            if string[i] in vowels and string[j] in vowels:
                # Swap vowels
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
            elif string[i] not in vowels:
                i += 1  # Move left pointer forward
            elif string[j] not in vowels:
                j -= 1  # Move right pointer backward

        return "".join(string)
