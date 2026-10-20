class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        maxx = 0 
        while i < j:
            area =(j-i) * min(heights[i], heights[j]) 
            maxx = max(area, maxx)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxx