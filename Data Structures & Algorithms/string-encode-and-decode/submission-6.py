class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += f"{len(word)}" + "#" + word

        return ans

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        answer = []
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            answer.append(word)
            i = j+1+length
        
        return answer
            