class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        n = len(s)
        freqs = [0] * 26
        longest = 0
        for r in range(n):
            freqs[ord(s[r])-ord('A')] += 1
            while (r-l) + 1 - max(freqs) > k:
                freqs[ord(s[l])-ord('A')] -= 1
                l += 1
            
            longest = max((r-l)+1, longest)

        return longest