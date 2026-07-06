class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left, prod = [], 1
        for i, num in enumerate(nums):
            prod *= num
            left.append(prod)
        
        right, prod = [], 1
        for i, num in enumerate(nums[::-1]):
            prod *= num
            right.append(prod)
        right = right[::-1]

        output = []
        for i in range(n):
            if i == 0:
                output.append(right[i+1])
            elif i == n-1:
                output.append(left[i-1])
            else:
                output.append(left[i-1] * right[i+1])
        
        return output