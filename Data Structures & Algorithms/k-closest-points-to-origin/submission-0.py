import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        for i, point in enumerate(points):
            distance = ((point[0] ** 2) + (point[1] ** 2)) ** 0.5
            heapq.heappush(max_heap, (-distance, i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        output = []
        for tup in max_heap:
            output.append(points[tup[1]])
        
        return output