class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        n = len(numbers)
        r = n - 1
        while l <= r:
            s = numbers[l] + numbers[r]
            if s != target:
                if s > target:
                    r -= 1
                else:
                    l += 1

            else:
                return [l+1, r+1]