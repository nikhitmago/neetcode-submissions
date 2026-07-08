import math
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = ""

        min_len = math.inf
        for string in strs:
            min_len = min(min_len, len(string))
        
        for i in range(min_len):
            set_letter = set(string[i] for string in strs)
            if len(set_letter) == 1:
                lcp += string[i]
            else:
                break
        
        return lcp