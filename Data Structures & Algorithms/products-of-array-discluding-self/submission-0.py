class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n):
            otp=1
            for j in range(n):
                if j!=i:
                    otp*=nums[j]
            res.append(otp)
        return res