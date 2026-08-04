class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    
        window_sum = 0
        for i in range(k):
            window_sum += abs(arr[i] - x)
        min_idx = (0, k-1)
        min_sum = window_sum
        
        l, n = 0, len(arr)
        for r in range(k, n):
            window_sum += abs(arr[r] - x)
            window_sum -= abs(arr[l] - x)

            l += 1

            if window_sum < min_sum:
                min_sum = window_sum
                min_idx = (l, r)
        
        return arr[
            min_idx[0]
            :
            min_idx[1] + 1
        ]