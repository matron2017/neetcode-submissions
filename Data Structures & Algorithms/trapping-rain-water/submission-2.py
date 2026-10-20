class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_height = 0
        r_height = 0
        left_max = [0] * n
        right_max = [0] * n

        for i in range(n):
            j = -i - 1
            left_max[i] = l_height
            right_max[j] = r_height
            l_height = max(l_height, height[i])
            r_height = max(r_height, height[j])

        summ = 0

        for i in range(n):
            pot = min(left_max[i], right_max[i])
            summ += max(0, pot - height[i])
        
        return summ