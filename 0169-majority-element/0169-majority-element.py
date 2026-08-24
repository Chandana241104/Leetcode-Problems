class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                a[nums[i]]+=1
        for i in a:
            if a[i]>(n//2):
                return i