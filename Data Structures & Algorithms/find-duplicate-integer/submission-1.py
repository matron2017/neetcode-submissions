class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        new_slow = 0
        while new_slow != slow:
            new_slow = nums[new_slow]
            slow = nums[slow]
        return new_slow
            