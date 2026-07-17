class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in range(n):
            left=len(set(nums[:i+1]))
            right=len(set(nums[i+1:]))
            a.append(left-right)
        return a

        