"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        intervals = [(0,40),(5,10),(15,20)]
        start = [0, 5, 15]
        end = [10, 20, 40]
        '''
        
        n = len(intervals)
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        count, res = 0, 0
        s_idx, e_idx = 0, 0

        while s_idx < n:
            if start_times[s_idx] < end_times[e_idx]:
                s_idx += 1
                count += 1
            else:
                e_idx += 1
                count -= 1
            res = max(res, count)
        
        return res