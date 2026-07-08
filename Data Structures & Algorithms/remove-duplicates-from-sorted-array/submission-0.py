class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # [0, 0, 1, 1, 1, 2, 2, 3, 4]

        n = len(nums)
        l = r = 1

        while r < n:
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l
