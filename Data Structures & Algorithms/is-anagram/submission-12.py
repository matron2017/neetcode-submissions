from collections import defaultdict
class Solution:
    #remember to unice first and last, how to make it to the numbers we want
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)
        
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1

        
        for count in counter.values():
            if count != 0:
                return False
            
        return True
        

