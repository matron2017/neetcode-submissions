from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        n = len(nums)
        buckets = [0] * (n+1)  

        for num, freq in freqs.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ans = []

        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ans.extend(buckets[i])
            if len(ans) == k:
                break

        return ans
