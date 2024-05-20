class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        singles = []
        doubles = []
        temp = []

        for num in nums:
            if num not in singles:
                singles.append(num)
                temp.append(num)
            elif num not in doubles:
                doubles.append(num)
                temp.append(num)
            else:
                pass

        nums[:] = temp
        
        return len(nums)