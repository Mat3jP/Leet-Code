class Solution:
    #def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        num = 0
        weight = 1
        i = -1
        while (abs(i)<=len(digits)):
            num += digits[i]*weight
            weight*=10
            i -= 1
        num+=1
        digits = []
        for the in str(num):
            digits.append(int(the))
        return digits
