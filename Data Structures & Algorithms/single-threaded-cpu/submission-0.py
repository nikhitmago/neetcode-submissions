import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ''' 
        time = 6
        res = [3,4,2,0]
        
        enque_heap = []
        
        proc_heap = [2,0], [4,1]
        
        '''

        enque_heap = [[task[0], task[1], i] for i, task in enumerate(tasks)]
        heapq.heapify(enque_heap)  # (enque_time, proc_time, index)
        proc_heap = []  # (proc_time, index)

        time = 0
        res = []
        while enque_heap or proc_heap:
            time += 1

            while enque_heap and enque_heap[0][0] <= time:
                _, proc_time, index = heapq.heappop(enque_heap)
                heapq.heappush(proc_heap, (proc_time, index))
            
            if proc_heap:
                proc_time, index = heapq.heappop(proc_heap)
                res.append(index)
                time += (proc_time - 1)
        
        return res