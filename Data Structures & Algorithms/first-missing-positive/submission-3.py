class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=1
        if len(nums)<=1:
            if nums[0]>1:
                return 1
            else:
                return 2
        for i in range(len(nums)):
            if n not in  nums:
                return n
            n+=1
        return max(nums)+1


        
            


