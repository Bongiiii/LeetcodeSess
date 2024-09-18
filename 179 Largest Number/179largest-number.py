class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Understand:
        Input: A list of non-negative integers nums.
        Output: A string representing the largest number possible when the integers are concatenated.
        Constraints:
        We are working with integers, but the challenge is to find the correct order for concatenating 
        them as strings to form the largest number.
        Handle cases where multiple integers are 0 (e.g., [0, 0] should return "0", not "00").

        Match:
        This problem requires a custom sorting approach because the natural sorting 
        of integers (i.e., numerical order) won’t necessarily give the largest possible concatenated result.

        Key steps:

        Convert all integers into strings for concatenation purposes.
        Sort the strings based on how they compare when concatenated in different orders.
        For two numbers x and y, compare x + y vs. y + x as strings, and place the larger concatenation first.
        We don’t need complex data structures, but we need to focus on sorting with a custom comparator.

        Plan:
        Convert Integers to Strings: Since the key to solving this problem is to determine how 
        two numbers concatenate as strings, we need to treat the numbers as strings during the sorting process.

        Sort with Custom Comparison: To sort the numbers, use a custom sorting rule: for any two
        numbers x and y, compare x + y vs. y + x. If x + y is larger, x should come before y; otherwise, y 
        should come first.

        Concatenate the Sorted Strings: Once sorted, join the list of strings to form the final result.

        Handle Edge Case: If the largest number is 0 (i.e., if the sorted result begins with a '0'), 
        return '0' to avoid cases like "00".

        Review:
        Time Complexity:

        The most expensive operation is sorting the list of strings. Sorting has a time complexity
        of O(N log N), where N is the number of elements in the list.
        In the custom sorting comparison, each comparison is O(1) because we are only comparing the 
        concatenation of two numbers.
        
        Space Complexity:

        The space complexity is O(N) because we create a list of strings and then join them into a 
        single result string.
        Edge Cases:

        If all the numbers are zeros (e.g., [0, 0]), the function correctly handles this by checking if
        the first character of the result is '0' and returning '0' in such cases.
        The function works even when there's only one element in the list.
        """
        # Convert the numbers to strings
        nums = list(map(str, nums))

        # Sort the numbers using custom comparison (concatenating x+y and y+x)
        nums.sort(key=lambda x: x*10, reverse=True)  # *10 is a trick to handle edge cases with shorter strings
        
        # Concatenate the sorted numbers
        result = ''.join(nums)

        # If the result starts with '0', return '0' (this handles cases like [0, 0])
        return '0' if result[0] == '0' else result   

            
