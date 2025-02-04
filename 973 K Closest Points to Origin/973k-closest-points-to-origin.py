from typing import List
from heapq import nsmallest

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        solving the problem using the heapq/ min heap approach and euclidean approach

        R/E:
        s/c = O(k)
        t/c = O(Nlogk)

        """
        #helper function to calculate distance
        def dist(point):
            return (point[0]**2) + (point[1]**2)

        #return statement literally reads, return the smallest k elements from data set/array points and sort them according to the distances
        return nsmallest(k,points,key=dist)