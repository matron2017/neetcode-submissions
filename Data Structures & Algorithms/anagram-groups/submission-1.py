class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #tuple with 0-25 keys index (26 really)
        #ors('') # unicode keys match if same
        past = {}

        # for mark everything into the dict one by one
        # by counting their unicode ascii list
        # and turn that to tuple key
        for n in range(len(strs)):
            count = [0] * 26
            word = strs[n]
            for char in word:
                count[ord(char)-ord('a')] += 1
            key = tuple(count)
            if not key in past:
                past[key] = [word]
            else:
                past[key].append(word)
        return list(past.values())