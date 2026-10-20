from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = (n+1)*[0]
        counts = Counter(nums)
        
        for num, freq in counts.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ans = []

        for values in buckets[::-1]:
            if values != 0:
                ans.extend(values)
            if len(ans) == k:
                break
        
        return ans
            
            

            
