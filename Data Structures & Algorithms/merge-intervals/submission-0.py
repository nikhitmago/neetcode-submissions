class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        [1,3], [4,5], [6,7]
        '''

        intervals.sort(key=lambda x: x[0])

        n = len(intervals)
        res = []
        i = 0

        merged_interval = intervals[0]
        for i in range(1, n):
            if merged_interval[1] >= intervals[i][0]:
                merged_interval[0] = min(merged_interval[0], intervals[i][0])
                merged_interval[1] = max(merged_interval[1], intervals[i][1])
            else:
                res.append(merged_interval)
                merged_interval = intervals[i]
        
        res.append(merged_interval)
        return res