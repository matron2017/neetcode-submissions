class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        n = len(nums)
        bucket = [0] * (n + 1)

        for num, freq in counts.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        # [1, 2, 3]
        # [0, 1, 2, 3]
        top_k = []
        #rememebr, the max index is alwasy length -1 (indexing from 0)
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                top_k.extend(bucket[i])
            if len(top_k) == k:
                return top_k



