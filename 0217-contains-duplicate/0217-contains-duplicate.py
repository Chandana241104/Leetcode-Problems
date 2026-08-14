class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                return True
        return False