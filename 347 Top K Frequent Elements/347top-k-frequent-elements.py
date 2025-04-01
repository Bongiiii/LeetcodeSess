from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)

        heap = heapq.nlargest(k,numsCounter.items(), key=lambda item:item[1])

        res = [x[0] for x in heap]

        return res
        