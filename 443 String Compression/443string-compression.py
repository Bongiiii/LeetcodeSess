class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer for where to write in the array
        i = 0  # Pointer for reading through the array

        while i < len(chars):
            char = chars[i]
            count = 0

            # Count the length of the group of the same character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            # Write the character to the write pointer
            chars[write] = char
            write += 1

            # If the count is more than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write  # This is the new length of the compressed array
