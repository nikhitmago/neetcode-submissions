class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [0,1,2,3,4,5,6] // i
        [0,8,0,6,5,9,8] // temperatures

        (9, 5) // new (temp, i)

        (v, i) // stack
        (5, 4)
        (6, 3)
        (8, 1)
        
        [0,1,2,3,4,5,6] // i
        [1,4,1,2,1,0,0] // res
        '''

        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and (temp > stack[-1][0]):
                pop_val, pop_idx = stack.pop()
                res[pop_idx] = i - pop_idx
            
            stack.append((temp, i))
        
        return res