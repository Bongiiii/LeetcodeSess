class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Understand:
        input - array of integers and an integer, output - integer

        Match:
        hash map for efficient pair matching

        Plan:
        - Use a hash map to store counts of numbers seen so far.
        - For each number in the array:
            - Check if `k - num` exists in the hash map:
                - If it does, increment the count and decrement the hash map value for `k - num`.
                - Otherwise, add the current number to the hash map or increment its count.
        - Return the total count.

        R/E:
        s/c = O(N), for the hash map.
        t/c = O(N), for iterating through the array.
        """
        freq = {}
        count = 0

        for num in nums:
            complement = k - num
            if complement in freq and freq[complement] > 0:
                count += 1
                freq[complement] -= 1  # Use one instance of the complement
            else:
                freq[num] = freq.get(num, 0) + 1  # Store the current number

        return count
