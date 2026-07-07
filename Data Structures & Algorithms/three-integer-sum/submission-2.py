class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        target = 0
        nums.sort()

        # [-4, -1, -1, 0, 1, 2]

        n = len(nums)
        output = []
        
        for i in range(n):
            if nums[i] > 0:
                break
            
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            
            l, r = i+1, n-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < target:
                    l += 1
                elif three_sum > target:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (l < r) and (nums[l] == nums[l-1]):
                        l += 1
        
        return output
