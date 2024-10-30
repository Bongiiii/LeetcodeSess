class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on end time to use the greedy approach
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        count = 0  # to count removals
        prev_end = intervals[0][1]  # end of the first interval
        
        # Iterate from the second interval onward
        for i in range(1, len(intervals)):
            # If current interval starts before the previous end, it overlaps
            if intervals[i][0] < prev_end:
                count += 1  # we need to remove an interval
            else:
                # No overlap, so update prev_end to current interval's end
                prev_end = intervals[i][1]
        
        return count