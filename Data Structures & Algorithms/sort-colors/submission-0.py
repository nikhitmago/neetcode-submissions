class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = 8
        # [0,1,2,3,4,5,6,7] // i
        # [0,1,2,1,1,0,2,2] // nums
        # l, r = (0, 7)

        

        n = len(nums)
        l, r = 0, n-1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:  # nums[i] == 2
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1