class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        duplicate = 0

        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
            if map[ele] >= 2:
                duplicate = ele
                break

        return duplicate