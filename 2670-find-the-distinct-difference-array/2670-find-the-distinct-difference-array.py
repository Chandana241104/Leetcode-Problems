class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        s=set()
        for i in range(n):
            s.add(nums[i])
            prefix[i]=len(s)
        s=set()
        for i in range(n-1,-1,-1):
            s.add(nums[i])
            suffix[i]=len(s)
        ans=[0]*n
        for i in range(n):
            if i==n-1:
                ans[i]=prefix[i]
            else:
                ans[i]=prefix[i]-suffix[i+1]
        return ans  
        