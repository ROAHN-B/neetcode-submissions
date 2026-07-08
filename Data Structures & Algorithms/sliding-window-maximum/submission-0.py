class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        window = []
        output = []


        while r <= len(nums):
            for ele in range(l, r):
                window.append(nums[ele])
            output.append(max(window))
            window.clear()
            l += 1
            r += 1
        return output
