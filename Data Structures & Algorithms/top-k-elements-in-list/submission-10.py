from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [0] * (n+1)
        counts = Counter(nums)

        for num, count in counts.items():
            if buckets[count] == 0:
                buckets[count] = [num]
            else:
                buckets[count].append(num)

        ans = []

        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ans.extend(buckets[i])
            
            if len(ans) == k:
                break
        
        return ans