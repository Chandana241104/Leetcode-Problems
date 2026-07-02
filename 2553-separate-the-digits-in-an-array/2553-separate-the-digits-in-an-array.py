class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            i=str(i)
            for j in range(len(i)):
                a.append(int(i[j]))
        return a