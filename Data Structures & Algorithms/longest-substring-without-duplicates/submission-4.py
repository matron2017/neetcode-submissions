class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        r = 0
        sett = set()
        l = 0
        longest = 0
        for i in range(n):
            r = i
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            sett.add(s[r])
            length = (r-l) + 1
            longest = max(length, longest)
        
        return longest


