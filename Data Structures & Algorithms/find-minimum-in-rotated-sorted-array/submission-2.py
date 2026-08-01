class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [0,1,2,3,4,5]
        # [3,4,5,1,2,3]
        
        n = len(nums)
        left, right = 0, n-1
        min_num = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                min_num = min(min_num, nums[left])
                break
            
            mid = left + (right - left) // 2
            min_num = min(min_num, nums[mid])

            # Left portion
            if nums[left] <= nums[mid]:
                left = mid + 1
            # Right portion
            else:
                right = mid - 1
        
        return min_num