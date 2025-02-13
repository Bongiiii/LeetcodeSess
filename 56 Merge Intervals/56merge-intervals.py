class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # Go through all intervals in sorted order
        for low, high in sorted(intervals):
            if not res or res[-1][1] < low:
                res.append([low, high])  # Start new interval
            else:
                res[-1][1] = max(res[-1][1], high)  # Merge intervals
                
        return res
