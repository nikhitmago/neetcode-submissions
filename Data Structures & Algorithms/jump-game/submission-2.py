class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True

        i, t = n-2, n-1

        while i >= 0:
            jumps_needed = t - i
            if nums[i] >= jumps_needed:
                t = i
            i -= 1
        
        return t == 0