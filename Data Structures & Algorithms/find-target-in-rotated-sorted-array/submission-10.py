class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,5,6,0,1,2]

        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # Left portion
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right portion
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1