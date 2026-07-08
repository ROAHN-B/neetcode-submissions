class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()

        if len(nums) % 2 ==0:
            return True
        else:
            return False