from collections import Counter, defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        xyxxyzbzbbisl

        counter = {
            x: 0
            y: 0
            z: 0
            b: 0
            i: 0
            s: 0
            l: 0
        }

        partitions = [
            {x: 3, y: 2},
            {z: 2, b: 3},
            {i: 1},
            {s: 1},
            {l: 1}
        ]
        '''

        counter = Counter(s)
        partitions = [defaultdict(int)]

        for char in s:
            partitions[-1][char] += 1
            counter[char] -= 1

            partition_count = sum([counter[key] for key in partitions[-1].keys()])
            if partition_count == 0:
                partitions.append(defaultdict(int))
        
        return [
            sum(partition.values())
            for partition in partitions[:-1]
        ]
