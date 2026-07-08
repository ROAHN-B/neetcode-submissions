class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod=0
        if len(nums) == 1:
            maxprod=nums[0]
        if len(nums) == 2:
            maxprod = nums[0] *nums[1]
        
        i=0
        j=i+1

        while (j<=len(nums)-1):
            maxprod = max(nums[i]*nums[j], maxprod)
            i+=1
            j+=1
        
        return maxprod
            