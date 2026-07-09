class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [0,1,2,2,3,0,4,2]

        k, n = 0, len(nums)
        
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k