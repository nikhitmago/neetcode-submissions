import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, sum, min_size = 0, 0, math.inf
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target and l <= r:
                min_size = min(min_size, r-l+1)
                sum -= nums[l]
                l += 1
        
        return 0 if min_size == math.inf else min_size