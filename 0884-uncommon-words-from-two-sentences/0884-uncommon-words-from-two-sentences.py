class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list1=[]
        s1=s1.split()
        s2=s2.split()
        for i in range(len(s1)):
            if s1[i] not in s2 and s1.count(s1[i])==1:
                list1.append(s1[i])
        for i in range(len(s2)):
            if s2[i] not in s1 and s2.count(s2[i])==1:
                list1.append(s2[i])
        return list1