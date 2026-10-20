class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointers apporach (slidiing window) l and r
        sett = set()
        l = 0
        n = len(s)
        longest = 0
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            sett.add(s[r])
            longest = max((r-l)+1, longest)

        return longest