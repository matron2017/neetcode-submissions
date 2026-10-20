class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #first easy case, just 2 for loops
        best_area = 0
        n = len(heights)
        l = 0
        r = n - 1
        while l < r:
            left, right = heights[l], heights[r]
            area = min(left, right) * abs(r-l)
            if area > best_area:
                best_area = area
            if left != right:
                if left > right:
                    r -= 1
                else:
                    l += 1
            else:
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
        return best_area