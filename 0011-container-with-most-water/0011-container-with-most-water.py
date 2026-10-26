class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        area1=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            area1=max(area1,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area1