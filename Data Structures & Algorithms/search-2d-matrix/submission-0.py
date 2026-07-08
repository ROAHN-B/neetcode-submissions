class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ele in matrix:
            if ele[0] <= target <= ele[-1]:
                l, r = 0, len(ele) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if ele[mid] == target:
                        return True
                    elif ele[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False

        return False