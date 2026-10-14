class Solution:
    def rev(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k%=n
        self.rev(nums,0,n-1)
        self.rev(nums,0,k-1)
        self.rev(nums,k,n-1)