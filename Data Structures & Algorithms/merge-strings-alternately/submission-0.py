class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n, m = len(word1), len(word2)
        i, j, k = 0, 0, 0
        res = ""

        while (i < n) and (j < m):
            res += word1[i]
            i += 1
            
            res += word2[j]
            j += 1
        
        while i < n:
            res += word1[i]
            i += 1
        
        while j < m:
            res += word2[j]
            j += 1
        
        return res