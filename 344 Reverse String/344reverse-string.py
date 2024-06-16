class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # use two pointers
        ptr1, ptr2 = 0, len(s) - 1

        while ptr1 <= ptr2:
            # swap the characters
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            #shift pointers
            ptr1 += 1
            ptr2 -= 1
