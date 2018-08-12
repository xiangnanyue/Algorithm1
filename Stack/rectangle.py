class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        stack = []
        height.append(0)
        area = 0
        for i, h in enumerate(height):
            if len(stack) == 0:
                stack.append(i)
                continue
            
            while len(stack) > 0:
                end = stack[-1]
                if h > height[end]:
                    stack.append(i)
                    break
                stack.pop()
                if len(stack) > 0:
                    width = i - 1 - stack[-1]
                else:
                    width = i
                area = max(area, height[end]*width)
            stack.append(i)
        return area
                        
            