import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        tasks = ["A","A","A","B","C"]
        n = 3

        heap = [1,1]  # cnt
        queue = [(2,4), ]  # (remaining_cnt, next_time)

        time = 1
        
        '''

        counter = Counter(tasks)
        
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)
        
        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = -heapq.heappop(max_heap)
                cnt -= 1
                if cnt > 0:
                    queue.append((cnt, time + n))
            
            if queue and queue[0][1] == time:
                remaining_cnt, _ = queue.popleft()
                heapq.heappush(max_heap, -remaining_cnt)
        
        return time



            