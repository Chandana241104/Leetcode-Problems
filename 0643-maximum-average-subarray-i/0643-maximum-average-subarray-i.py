class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sum2=float('-inf')
        # for i in range(0,len(nums)-k+1):
        #     sum1=sum(nums[i:i+k])
        #     avg=sum1/k
        #     sum2=max(sum2,avg)
        # return sum2
        curr_sum=sum(nums[:k])
        max_sum=curr_sum
        for i in range(k,len(nums)):
            curr_sum+=nums[i]-nums[i-k]
            max_sum=max(curr_sum,max_sum)
        return max_sum/k

        
