class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            summa = numbers[i] + numbers[j]
            if summa > target:
                    j -= 1
            elif summa < target:
                    i += 1
            else:
                return [i+1, j+1]