class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [0,1,2,3,4,5]
        # [4,5,0,1,2,3]
        
        n = len(nums)
        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]