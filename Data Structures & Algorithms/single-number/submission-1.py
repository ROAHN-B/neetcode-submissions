class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for ele in nums:
            dict[ele]=dict.get(ele,0)+1
        single=min(dict,key=dict.get)
        return single