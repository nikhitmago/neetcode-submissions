class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abba

        l = 2
        r = 3
        n = 4
        max_size = 2
        window = {a:0, b:2}

        '''
        

        n = len(s)
        if n == 0:
            return 0
        
        window = {}
        l, r, max_size = 0, 0, 0

        while r < n:
            if s[r] in window:
                l = max(l, window[s[r]] + 1)

            window[s[r]] = r
            max_size = max(max_size, r-l+1)

            r += 1

        return max_size