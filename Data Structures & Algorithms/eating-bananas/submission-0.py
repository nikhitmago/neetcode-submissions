class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
    
        def canEatWithinH(rate):
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / rate)
                if time_taken > h:
                    return False
            return True
        
        left, right = 1, max(piles)
        min_rate = max(piles)
        while left <= right:
            mid = (left + right) // 2

            if canEatWithinH(mid):
                right = mid - 1
                min_rate = mid
            else:
                left = mid + 1
        
        return min_rate