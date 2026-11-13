from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) #dict {number: counts}
        n = len(nums)
        freqs = [0]*(n + 1)

        for num, count in counts.items():
            if freqs[count] == 0:
                freqs[count] = [num]
            else:
                freqs[count].append(num)

        answer = []

        for i in range(n, -1, -1):
            if freqs[i] != 0:
                answer.extend(freqs[i])
            if len(answer) == k:
                break
        
        return answer