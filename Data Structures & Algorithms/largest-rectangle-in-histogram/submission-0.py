class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index #extend start index to the last value popped
            stack.append((start, h))

        #checking remaining entries, width = len hist. - i(value in stack)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

