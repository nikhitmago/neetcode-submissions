class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        res = [[1,2,3], [1,2], [1,3], [1]]
        
            [1]
        [1,2]   [1,3]
    [1,2,3] [1]



        '''
        
        res = []
        n = len(nums)
        
        def dfs(i, subset=[]):
            if i >= n:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(i+1, subset)

        dfs(0)
        return res 