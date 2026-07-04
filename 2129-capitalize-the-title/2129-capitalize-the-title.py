class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s=""
        for word in title.split():
            if len(word)<3:
                word=word.lower()
            else:
                word=word.title()
            s+=word+" "
        return s.strip()