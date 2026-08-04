class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        adc

        dcda
        '''

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_indices, s2_indices = [0] * 26, [0] * 26
        
        for i in range(n1):
            s1_indices[ord(s1[i]) - ord('a')] += 1
            s2_indices[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        for r in range(n1, n2):
            if s1_indices == s2_indices:
                return True
            
            s2_indices[ord(s2[l]) - ord('a')] -= 1
            s2_indices[ord(s2[r]) - ord('a')] += 1
            l += 1
        
        return s1_indices == s2_indices