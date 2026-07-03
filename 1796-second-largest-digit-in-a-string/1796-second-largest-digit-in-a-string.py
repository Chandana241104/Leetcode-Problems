class Solution:
    def secondHighest(self, s: str) -> int:
        max1=-1
        max2=-1
        for i in s:
            if i.isdigit():
                i=int(i)
                if i>max1:
                    max2=max1
                    max1=i
                elif i > max2 and i != max1:
                    max2=i
        return max2
                    
