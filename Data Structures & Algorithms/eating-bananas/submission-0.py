class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours_taken = 0
            for pile in piles:
                hours_taken += (pile + mid - 1) // mid

            if hours_taken <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans