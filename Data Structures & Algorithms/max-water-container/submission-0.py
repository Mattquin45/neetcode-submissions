class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        area = 0
        width = 0
        height = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res





        