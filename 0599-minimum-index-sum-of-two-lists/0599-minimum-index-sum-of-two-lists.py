class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a=[]
        sum1=float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    s=i+j
                    if s<sum1:
                        sum1=s
                        a=[list1[i]]
                    elif s==sum1:
                        a.append(list1[i])
        return a

