
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #freq = [0] * 26
        sublists = { } # make key the tuple, and the value the list of words
        for string in strs:
            freq = [0] * 26
            for i in range(len(string)):
                freq[ord(string[i])-ord('a')] += 1
            
            
            key = tuple(freq)
            if not key in sublists:
                sublists[key] = [string]
            else:
                sublists[key].append(string)
        
        return list(sublists.values())
            #strs[tuple(freq)] = strs.get(tuple(freq, [])).append()
            
        
                
