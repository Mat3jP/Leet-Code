class Solution:
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArray(self, nums1, nums2):
        list = sorted(nums1+nums2)
        total_len = len(list)

        print (f"{list}, {total_len}")

        if (total_len % 2 == 0):
            return (list[total_len//2]+list[(total_len//2)-1])/2
        else:
            return list[total_len//2]