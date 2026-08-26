class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        for ele in range(len(nums)-1):
            if nums.count(nums[ele])>len(nums)//2:
                output=nums[ele]
        return output