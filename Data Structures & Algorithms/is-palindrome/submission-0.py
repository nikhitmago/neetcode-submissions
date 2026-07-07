class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        preprocessed_s = ""
        for i, char in enumerate(s):
            if char.isdigit() or char.isalpha():
                preprocessed_s += char.lower()
            
        n = len(preprocessed_s)
        l, r = 0, n-1

        for i in range(n // 2):
            if preprocessed_s[l] != preprocessed_s[r]:
                return False    
            l += 1
            r -= 1
        
        return True