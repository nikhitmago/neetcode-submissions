class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        [4,1,2] // nums1
        d = {
            4: 0,
            1: 1,
            2: 2
        }

        [2,1,3,4] // nums2
        [-1,3,3] // res

        stack = [2,1] |3
        res = [-1,3,3]
        '''

        d = {}
        for i, num in enumerate(nums1):
            d[num] = i
        
        stack = []
        res = [-1] * len(nums1)
        for num in nums2:
            while stack and num > stack[-1]:
                pop_num = stack.pop()
                idx = d[pop_num]
                res[idx] = num

            if num in d:
                stack.append(num)
        
        return res