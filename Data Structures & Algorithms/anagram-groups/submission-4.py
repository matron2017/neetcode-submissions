
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for i in range(len(string)):
                freq[ord(string[i])-ord('a')] += 1
            
            sublists[tuple(freq)].append(string)
        
        return list(sublists.values())
     
            
        
                
