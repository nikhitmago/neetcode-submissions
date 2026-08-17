class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        output = 0
        last_end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] < last_end:
                output += 1
                last_end = min(last_end, intervals[i][1])
            else:
                last_end = max(last_end, intervals[i][1])
        
        return output