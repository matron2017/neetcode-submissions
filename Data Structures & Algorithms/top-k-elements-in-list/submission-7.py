from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        buckets = (n+1)*[0]
        
        for num, freq in counts.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        res = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                res.extend(buckets[i])
            if len(res) == k:
                break
        
        return res

            
