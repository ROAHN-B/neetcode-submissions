class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set={}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in set:
                lst1 = list((set[diff], i))
            set[num] = i
        return lst1
