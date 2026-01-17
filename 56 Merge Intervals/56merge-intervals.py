class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #start by sorting the intervals using the start time as the order of sorting
        intervals.sort(key=lambda x:x[0])
        
        #make res array
        res = []

        #grab the start and finish of the first interval
        cur_start, cur_end = intervals[0]
        
        for next_start, next_end in intervals[1:]:
            #no merge
            if cur_end < next_start:
                #add curr start and end to res
                res.append([cur_start, cur_end])

                #update curr with the next
                cur_start, cur_end = next_start, next_end

            #they overlap, hence update end of that interval
            cur_end = max(cur_end, next_end)

        res.append([cur_start, cur_end])

        return res
            