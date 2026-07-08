class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [-3, 0, 1, 2, 3, 3]; 3
        # [-1, -1, -1, 1, 1, 1]; 2

        nums.sort()
        n = len(nums)

        output = []
        for i in range(n-3):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            for j in range(i+1, n-2):
                if (j > i+1) and (nums[j] == nums[j-1]):
                    continue
                l = j+1
                r = n-1
                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum == target:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while (l < r) and (nums[l] == nums[l-1]):
                            l += 1
                        while (l < r) and (nums[r] == nums[r+1]):
                            r -= 1
                    elif four_sum < target:
                        l += 1
                    else:
                        r -= 1
        
        return output