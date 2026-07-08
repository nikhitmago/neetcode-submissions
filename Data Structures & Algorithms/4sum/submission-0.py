class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [-3, 0, 1, 2, 3, 3]; 3

        nums.sort()
        n = len(nums)

        output = set()
        for i in range(n-3):
            for j in range(i+1, n-2):                
                l = j+1
                r = n-1
                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum == target:
                        output.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif four_sum < target:
                        l += 1
                    else:
                        r -= 1
        
        return list(output)