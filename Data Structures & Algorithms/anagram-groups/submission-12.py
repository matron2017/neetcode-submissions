from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            bucket = [0] * 26
            for char in word:
                bucket[ord(char)-ord('a')] += 1
            groups[tuple(bucket)].append(word) 
        
        return list(groups.values())