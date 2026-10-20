class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        longest = 0
        l = 0
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            sett.add(s[r])
            longest = max((r-l)+1, longest)
            
        return longest
            # r = 4 ,  s[r] = x
            # l = 2 # y
            #sett = {x, z, y}
            # longest = 3
