class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=[]
        n=len(nums)
        left=0
        sum=0
        for i in range(n):
            sum+=nums[i]
        for i in range(n):
            x=abs(left-(sum-nums[i]-left))
            a.append(x)
            left+=nums[i]
        return a