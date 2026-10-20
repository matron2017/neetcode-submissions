class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past = set()
        for i in nums:
            if i in past:
                return True
            past.add(i)
        return False