class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1) - 1
        window = []
        substring = ""

        while j <= len(s2) - 1:
            while i <= j:
                window.append(s2[i])
                i += 1
            substring = "".join(window)
            window.clear()
            if sorted(substring) == sorted(s1):
                return True
                break

            i = j
            j += len(s1) - 1

        else:
            return False