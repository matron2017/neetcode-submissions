class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = len(numbers)
        r = n - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ > target:
                r -= 1
            elif summ < target:
                l += 1
            else:
                return [l+1, r+1]