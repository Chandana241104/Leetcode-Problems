class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=[]
        org=n
        while n>0:
            org=org%2
            n=n//2
            l.append(org)
            org=n
        for i in range(1,len(l)):
            if l[i-1]==l[i]:
                return False
        return True