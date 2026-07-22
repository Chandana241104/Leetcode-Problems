class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven=sumOdd=0
        for i in range(1,n*2):
            if i%2==0:
                sumEven+=i
            else:
                sumOdd+=i
        while sumOdd!=0:
            sumEven , sumOdd = sumOdd , sumEven % sumOdd
        return sumEven
