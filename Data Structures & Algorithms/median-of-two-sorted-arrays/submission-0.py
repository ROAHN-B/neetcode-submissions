class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 != 0:
            median = math.ceil(len(nums) / 2)
        else:
            median = (len(nums) + 1) / 2
        return median