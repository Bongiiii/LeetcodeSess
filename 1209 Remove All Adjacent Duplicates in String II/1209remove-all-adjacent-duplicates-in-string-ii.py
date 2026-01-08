class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        U:
        input - string, an integer variable

        given a string, crush/delete when string has k identical characters adjacent

        M:
        stack
        pointer/sliding window

        P:
        iterate string using pointers
        when you encouter consecutive identical characters
         modulo divide by k and pop stack when result is 0,
         else add that character and count to stack
         then add the resultant stack after removing identical adjacent characters
         and return resultant string

        I:
        R:
        s/c = O(n), n number of characters in string in worst case where you can crush anything
        t/c = O(n), n - length of string as we visit every character
        E:
        """
        crusher, i = [], 0

        while i < len(s):

            j = i

            while (j < len(s)) and s[j] == s[i]:
                j += 1

            neighbor_count = j - i
            mod_count = neighbor_count % k

            if crusher and crusher[-1][0] == s[i]:
                crusher[-1][1] = (crusher[-1][1] + mod_count) % k

                if crusher[-1][1] == 0:
                    crusher.pop()

            elif mod_count:
                crusher.append([s[i], mod_count])

            i = j

        res = [character * count for character, count in crusher]

        return "".join(res)

        