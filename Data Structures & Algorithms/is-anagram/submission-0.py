class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26

        #if we check how many alphanumerical for both
        # and they are the same bucket, then they are the same
        # thsi would take O(n) ?
        # Only need to  
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            index = ord(t[i]) - ord('a')
            if freq[index] == 0:
                return False
            freq[index] -= 1
        
        if sum(freq) > 0:
            return False
        return True
