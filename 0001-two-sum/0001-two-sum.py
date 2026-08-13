class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        a={}
        for i in range(n):
            complement=target-nums[i]
            if complement not in a:
                a[nums[i]]=i
            else:
                return [a[complement],i]