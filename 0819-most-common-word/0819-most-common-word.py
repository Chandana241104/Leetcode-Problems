class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        for ch in "!?',;.":
            paragraph=paragraph.replace(ch," ")
        words=paragraph.split()
        ans=""
        maximum=0
        for i in words:
            if i not in banned:
                c=words.count(i)
                if c>maximum:
                    maximum=c
                    ans=i
        return ans