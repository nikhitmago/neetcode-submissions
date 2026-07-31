class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 00, 01, 02, 03
        # 10, 11, 12, 13
        # 20, 21, 22, 23


        # n = 12, mid = 6, (i,j) = (1,2)
        # (// cols, % cols)
        # 0-3: (0,[0-3])
        # 4-7: (1,[0-3])
        # 8-11: (2,[0-3])

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            i, j = mid // n, mid % n

            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

