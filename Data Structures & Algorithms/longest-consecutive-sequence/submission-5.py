class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        #check if somethin smaller is in set,
        # if not ,start from here, otehrwise continue
        longest = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            length = 1
            curr_num = num + 1
            while curr_num in nums_set:
                length += 1
                curr_num += 1 

            longest = max(longest, length)

        return longest