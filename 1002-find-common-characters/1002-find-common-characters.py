class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=[]
        for ch in words[0]:
            found=True
            for i in range(1,len(words)):
                if ch not in words[i]:
                   found=False
                   break
            if found:
                common.append(ch)
                for i in range(1,len(words)):
                    words[i]=words[i].replace(ch,"",1)
        return common            