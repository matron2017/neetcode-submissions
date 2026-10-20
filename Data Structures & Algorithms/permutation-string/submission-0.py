class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        l = 0
        s1_lenght = len(s1)
        s1_freqs = [0] * 26
        s2_freqs = [0] * 26
        for s in s1:
            s1_freqs[ord(s)-ord('a')] += 1
        
        for r in range(n):
            s2_freqs[ord(s2[r]) - ord('a')] += 1 

            if s1_lenght > (r-l)+1:    
                continue

            if s2_freqs == s1_freqs:
                return True

            s2_freqs[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False
                
            

            
            
