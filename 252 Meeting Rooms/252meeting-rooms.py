class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Understand:
        input - array of arrays of integers, output - boolean

        Match:
        array manipulation
        two pointers

        Plan:
        initializa a pointer previous interval that takes the initial interval at index 0
        then start iterating from index 1 till the end of the array
        be checking each interval with the most previous interva;
        if intervals overlap, immediately return false, else update previous to the current interval and continue till the end of the array
        return true when no overlaps are found and array is exhausted

        R/E:
        s/c = O(1), 
        t/c = O(N), length of array
        """
        #base case, empty list, hence no meetings = no conflicts
        if not intervals:
            return True

        intervals.sort()
        prevInterval = intervals[0]

        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start < prevInterval[1]:
                return False


            prevInterval = [start, end]

        return True