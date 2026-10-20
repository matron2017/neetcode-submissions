class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        maxx = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxx = max(area, maxx)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxx


