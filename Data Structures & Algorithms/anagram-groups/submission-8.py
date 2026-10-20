from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #remember to explain what immutable means.
        if len(strs) == 0: #maybe not needed
            return [[""]]
        
        anagrams = defaultdict(list)

        for word in strs:
            counts = 26*[0]
            for char in word:
                counts[ord(char)- ord('a')] += 1
            
            anagrams[tuple(counts)].append(word)
        

        return list(anagrams.values())
