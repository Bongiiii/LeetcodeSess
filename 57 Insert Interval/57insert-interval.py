class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Understand:
        input - 2d array(array of arrays), output - array of arrays
        Prob summary: given a 2d array of intervals, merge the overlapping intervals and return the resultant array after merging overlapping intervals

        Match:
        2d arrays

        Plan:
        put the elements in the intervals array into a hashmap, start as key and end as value
        check if start of new interval is in the hashmap keys, then use the min between the key start and the start in hand as use athe resultant start
        period and the end will be the max between value in hashmap and the end in the interval period 
        then append the min and max into a resultant array to return the merged time interval 
        """
        res = []
        
        for i in range(len(intervals)):
            # If the current interval ends before newInterval starts, add it to the result
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # If the current interval starts after newInterval ends, add newInterval and reset it
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]
            # Overlapping intervals, merge by adjusting newInterval's start and end
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # Add the last interval
        res.append(newInterval)
        
        return res