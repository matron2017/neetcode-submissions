class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if not numbers[l] + numbers[r] == target:
                if numbers[l] + numbers[r] > target:
                    r -= 1
                    continue
                l += 1

            else:
                return [l+1, r+1]
        
