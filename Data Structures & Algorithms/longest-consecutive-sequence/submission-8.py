class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        for num in nums_set:
            if (num-1) in nums_set:
                continue
            
            length = 1
            while (num+1) in nums_set:
                length += 1
                num += 1
            
            longest = max(length, longest)

        return longest