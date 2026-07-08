class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=[]
        if not nums:
            return 0
        else:
            nums.sort()
            n=len(nums)
            index=nums[0]

            for i in nums:
                if index == i:
                    res.append(i)
                    index+=1
                else:
                    i+=1
            return (len(res))