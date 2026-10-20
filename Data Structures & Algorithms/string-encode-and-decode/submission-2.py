class Solution:
        # example: 
        # [neet, co#de]
        # -> "4#neet5#co#de"
        # -> [neet, co#de]
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + "#" + word
        return ans


    def decode(self, s: str) -> List[str]:
        ans, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            ans.append(word)
            i = j+1+length

        return ans