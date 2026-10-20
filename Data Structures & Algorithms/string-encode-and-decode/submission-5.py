class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans = ans + str(len(word)) + "#" + word
        return ans
        
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        ans = []
        while i < n:
            j = i 
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1: j+1+length]
            ans.append(word)
            i = j+1+length

        return ans 

        
