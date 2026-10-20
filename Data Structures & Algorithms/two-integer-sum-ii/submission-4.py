class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            summed = numbers[r] + numbers[l]
            if target != summed:    
                if summed > target:
                    r -= 1
                else:
                    l += 1
            else:
                return [l+1, r+1]


