class Solution:
    #remember to unice first and last, how to make it to the numbers we want
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {} # key is char, value is count
        if len(s) != len(t):
            return False
        
        count_s = [0] * 26
        count_t = [0] * 26
        
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1
        
        if count_s == count_t:
            return True

        return False
        

