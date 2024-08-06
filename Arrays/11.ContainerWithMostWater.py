class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            minHeight = min(height[left], height[right])
            area = max(area, minHeight * abs(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

aa = Solution()
print(aa.maxArea(height =[1,8,6,2,5,4,8,3,7]))