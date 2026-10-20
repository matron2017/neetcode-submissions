from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [0] * (n + 1)
        counts = Counter(nums) # key is num, value is count
        
        for num, count in counts.items():
            if bucket[count] == 0:
                bucket[count] = [num]
            else:
                bucket[count].append(num)
        
        ans = []
        for i in range(n, 0, -1):
            if bucket[i] != 0:
                ans.extend(bucket[i])
            if len(ans) >= k:
                break
        return ans



            
