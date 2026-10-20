from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        bucket = [0] * (n+1)

        for number, freq in counts.items():
            if bucket[freq] == 0:
                bucket[freq] = [number]
            else:
                bucket[freq].append(number)
        ret = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                ret.extend(bucket[i])
            if len(ret) == k:
                break
        return ret