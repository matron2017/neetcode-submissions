class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check alwasy if there is past
        # if not start,  otherwise not
        # and count longest
        # make a set of it
        # and go throgh, always check if exists.
        # [2, 20, 4, 10, 3, 4 ,5]
        #
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            length = 1
            count = num
            while (count + 1) in nums_set:
                length += 1
                count += 1
            
            longest = max(length, longest)
        
        return longest