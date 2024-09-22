import random
import bisect

class Solution:
    """
    Understand:
    Input: A list w where w[i] represents the weight of index i.

    Output: A random index is picked, but the probability of picking each index is proportional to its weight.

    For example, if w = [1, 3, 2], index 0 should have a probability of 1/(1+3+2) = 1/6, index 1 should have
     3/6 = 1/2, and index 2 should have 2/6 = 1/3.

    Match:
    Concept: This problem is a weighted random selection problem.
    Algorithm:
    We can use prefix sums to convert the weights into cumulative probabilities.
    Binary search can be used to efficiently find which range the random number falls into.
    Random number generation helps simulate picking based on these weights.

    Plan:
    Precompute Prefix Sums: Create an array of cumulative sums where each element represents the sum of 
    weights up to that index.
    Generate Random Number: Pick a random number between 1 and the total sum of weights.
    Binary Search: Use binary search on the prefix sum array to find the smallest index whose cumulative 
    weight is greater than or equal to the random number.
    Return the Index: The corresponding index is the one whose weight the random number falls within.

    R/E (Run and Evaluate):
    Space Complexity: O(n) for storing the prefix sum array.
    Time Complexity:
    O(n) for initializing the prefix sums.
    O(log n) for selecting the index using binary search during each call to pickIndex().
    """

    def __init__(self, w: List[int]):
         # Precompute prefix sums of weights
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

       
    def pickIndex(self) -> int:
         # Pick a random number in the range [1, total_sum]
        target = random.randint(1, self.total_sum)
        
        # Find the index using binary search (bisect)
        return bisect.bisect_left(self.prefix_sums, target)
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()