from collections import defaultdict

# [0,1,2,3,4,5,6]

class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.d.get(key, [])
        res = ""
        
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] == timestamp:
                return nums[mid][1]
            
            if nums[mid][0] < timestamp:
                res = nums[mid][1]  # smallest value if not found in the right most side
                left = mid + 1
            else:
                right = mid - 1
        
        return res