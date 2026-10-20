class Solution:
    #remember to unice first and last, how to make it to the numbers we want
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {} # key is char, value is count
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False

        return True
        

