from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

        k_sorted_d = sorted_d[:k]
        return [key for key, value in k_sorted_d]