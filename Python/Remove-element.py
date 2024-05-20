class Solution:
    #def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):
        left = len(nums)

        while val in nums:
            nums.remove(val)
            left -= 1

        return left