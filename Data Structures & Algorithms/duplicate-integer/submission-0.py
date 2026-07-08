class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst1=set(nums)
        if len(lst1)==len(nums):
            return False
        else:
            return True