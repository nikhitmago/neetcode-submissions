from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        0 12345 6
        A AABAB B

        l = 1
        r = 5
        res = 5

        window = {A:3, B:2}
        mf_val = 4
        window_size = 6
        '''

        window = defaultdict(int)
        l, r, n = 0, 0, len(s)

        def getMostFreqVal():
            window_sorted = sorted(window.items(), key=lambda x: x[1], reverse=True)
            return window_sorted[0][1]

        res = 0
        while r < n:
            window[s[r]] += 1
            mf_val = getMostFreqVal()

            while (r - l + 1) - mf_val > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res