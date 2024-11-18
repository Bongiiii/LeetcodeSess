class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Understand:
        input - circular array of integers, integer; output - array of integers
        Edge cases: array with only one element

        Match:
        array manipulation
        sliding window

        Plan:
        Initialize an output array for cases where k != 0.
        For k = 0, return an array of the same length with all elements as 0 (early return).
        Based on the sign of k:
        - If k > 0, sum the next k elements for each index.
        - If k < 0, sum the previous k elements for each index (wrap around using modulus).

        Using sliding window:
        - The sign of k determines the direction of traversal.
        - +ve k sums forward, -ve k sums backward.

        Time complexity: O(N), where N is the size of the input array.
        Space complexity: O(N), for the output array.
        """

        n = len(code)
        output = [0] * n

        # Base case: k == 0
        if k == 0:
            return output

        # Sliding window approach
        window_sum = 0
        #traversal directions for the windowsum
        start, end = (1, k) if k > 0 else (n + k, n - 1)

        # Precompute the initial window sum
        for i in range(start, end + 1):
            #modulo division for the wrap around, circular effect
            window_sum += code[i % n]

        for i in range(n):
            #replacement
            output[i] = window_sum
            # Slide the window
            window_sum -= code[(start) % n]
            start += 1
            end += 1
            window_sum += code[end % n]

        return output
