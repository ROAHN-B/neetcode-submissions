class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res={}
        output=[]
        times=len(nums)//3
        for ele in nums:
            res[ele]=1+res.get(ele,0)
            if res[ele] == times + 1:
                output.append(ele)

        return output