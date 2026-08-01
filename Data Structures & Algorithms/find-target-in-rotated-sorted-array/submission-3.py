class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2]

        n = len(nums)

        def find_pivot():
            left, right = 0, n-1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2

                if target == nums[mid]:
                    return mid
                
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        # Main Guy
        pivot = find_pivot()
        if nums[pivot] == target:
            return pivot
        
        left_val = binary_search(0, pivot-1)
        if left_val != -1:
            return left_val
        
        right_val = binary_search(pivot, n-1)
        if right_val != -1:
            return right_val
        
        return -1