class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(nums, target):
        list = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                if target - nums[j] - nums[i] == 0 and i != j:
                    list.append(i)
                    list.append(j)
                    return list
