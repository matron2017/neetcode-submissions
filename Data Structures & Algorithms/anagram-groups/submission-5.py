class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            freqs = [0] * 26
            for index, char in enumerate(word):
                freqs[ord(char)-ord('a')] += 1
            freq_key = tuple(freqs)

            if freq_key in anagrams:
                anagrams[freq_key].append(word)
            else:
                anagrams[freq_key] = [word]
        
        return list(anagrams.values())