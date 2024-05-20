class Solution:
    #def trailingZeroes(self, n: int) -> int:
    def trailingZeros(self, n):
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros