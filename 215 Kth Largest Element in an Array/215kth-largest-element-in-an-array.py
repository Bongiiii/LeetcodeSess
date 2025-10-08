from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        create a max heap using heapify
        """
        res = [-x for x in nums]
        heapify(res)

        for _ in range(k-1):
            heappop(res)

        return -res[0]