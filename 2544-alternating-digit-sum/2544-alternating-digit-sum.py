class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        ans = 0
        sign = 1

        for d in digits:
            ans += int(d) * sign
            sign *= -1

        return ans
        