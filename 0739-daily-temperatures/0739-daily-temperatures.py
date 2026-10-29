class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                previous_index=stack.pop()
                ans[previous_index]=i-previous_index
            stack.append(i)
        return ans
        