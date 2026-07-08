class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1, 2, 2, 3, 3]

        people.sort()
        
        n = len(people)
        l, r = 0, n-1

        count = 0
        while l <= r:
            if people[l] == limit:
                count += 1
                l += 1
                continue

            if people[r] == limit:
                count += 1
                r -= 1
                continue
            
            two_sum = people[l] + people[r]
            if two_sum <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                count += 1
                r -= 1 
        
        return count
