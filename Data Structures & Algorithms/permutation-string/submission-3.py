class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n2 = len(s2)
        n1 = len(s1)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1 
        if s2_counts == s1_counts:
                return True
        l = 0
        r = n1 

        #while r < n2:
        for r in range(n1, n2):
            s2_counts[ord(s2[r]) - ord('a')] += 1
            s2_counts[ord(s2[l]) - ord('a')] -= 1
            if s2_counts == s1_counts:
                return True
            l += 1

        return False
                
            

            
            
