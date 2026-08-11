import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while True:
            if len(max_heap) == 0:
                return 0
            if len(max_heap) == 1:
                return -max_heap[0]

            diff = heapq.heappop(max_heap) - heapq.heappop(max_heap)
            if diff < 0:
                heapq.heappush(max_heap, diff)