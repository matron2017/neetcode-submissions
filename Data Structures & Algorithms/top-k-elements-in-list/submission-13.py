from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [0] * (n+1)
        freqs = Counter(nums)

        for num, freq in freqs.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        answer = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                answer.extend(buckets[i])
            if len(answer) >= k:
                break

        return answer


