class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)

        longest = 1
        streak = 1
        for i in range(n-1):
            if nums[i+1] - nums[i] == 0:
                continue
            elif nums[i+1] - nums[i] == 1:
                streak += 1
            else:
                longest = max(streak, longest)
                streak = 1
        
        return max(streak, longest)
            