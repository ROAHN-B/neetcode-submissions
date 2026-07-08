class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        found=False
        for i in range(len(s2) - len(s1) + 1):
                substring = s2[i : i + len(s1)]
                if sorted(substring) == sorted(s1):
                    found = True
                    return found
                    break
        if not found:
            return found