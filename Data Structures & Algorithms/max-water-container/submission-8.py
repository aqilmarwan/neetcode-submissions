class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #2 pointers, no need to sort, l, r.
        result = 0
        l, r = (0, len(heights) - 1)

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(result, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return result