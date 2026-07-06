class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        sizes = [str(len(string)) for string in strs]
        sizes_str = ",".join(sizes)
        sizes_str += ",#"
        encoded += sizes_str

        letters = ""
        for string in strs:
            letters += string
        encoded += letters
        
        return encoded


    def decode(self, s: str) -> List[str]:
        
        i, n, sizes = 0, len(s), []
        while i < n:
            if s[i] == "#":
                i += 1
                break
            if s[i] == ",":
                i += 1
                continue
            
            num = ""
            while s[i].isdigit():
                num += s[i]
                i += 1

            sizes.append(int(num))
        
        decoded = []
        for size in sizes:
            decoded.append(s[i:i+size])
            i += size
        
        return decoded
        
