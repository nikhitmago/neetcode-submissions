class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n

        for _ in range(k):
            l, r = 0, n-1
            temp = nums[r]
            
            while l < r:
                nums[r] = nums[r-1]
                r -= 1
            
            nums[l] = temp
