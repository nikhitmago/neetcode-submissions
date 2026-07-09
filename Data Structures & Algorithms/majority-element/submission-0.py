class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # boyer-moore algo: increment counter every time you see X, decrement when you dont
        # since majority is > n/2, the majority element will be the only one that survives

        res = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                res = num
            
            if num == res:
                count += 1
            else:
                count -= 1

        return res