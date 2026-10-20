class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #tuple with 0-25 keys index (26 really)
        #ors('') # unicode keys match if same
        bucket = [0] * 26
        past = {}

        # for mark everything into the dict one by one
        # by counting their unicode ascii list
        # and turn that to tuple key
        for n in range(len(strs)):
            bucket = [0] * 26
            for char in strs[n]:
                bucket[ord(char)-ord('a')] += 1
            key = tuple(bucket)
            if not key in past:
                past[key] = [strs[n]]
            else:
                past[key].append(strs[n])
        return list(past.values())