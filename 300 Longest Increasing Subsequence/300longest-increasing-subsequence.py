import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Understanding:
        input - unsorted array of integers, output - integer
        problem summary: given an unsorted array of integers, find the longest increasing subsequence of integers

        Clarfying questions:
        does the subsequence need to be contiunous?

        Match:
        dp
        binary search

        Plan:
        no need to cater for empty array as constraints state that atleast one element is present
        initiate a dp array to store the smallest tail
        to incorporate binary search, make use of bisect_left to be identifying index 
         of elements in dp array and comparing with input array elements
        use the bisect_left method to find the index we could potentially put an element if it is increasing
        compare index with len(dp)
        if index is the same as length of dp, then append num
        else, override/replace element at that index with num
        return length of dp array after iterating through the whole array

        R/E:
        s/c = O(N), length of dp array
        t/c = O(Nlogn), length of input array * binary search time taken
        """
        dp = []

        for num in nums:
            index = bisect.bisect_left(dp, num)

            if index == len(dp):
                dp.append(num)

            else:
                dp[index] = num

        return len(dp)
        