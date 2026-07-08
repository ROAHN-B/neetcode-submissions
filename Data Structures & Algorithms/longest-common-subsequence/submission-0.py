class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count=0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text2[j] == text1[i]:
                    count+=1
                else:
                    j+=1
            i+=1
        return count
