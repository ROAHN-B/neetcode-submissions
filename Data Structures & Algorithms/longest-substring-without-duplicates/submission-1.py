class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return len(s)
        else:
            substring = set()
            l= 0
            for r in range(len(s)):
                while s[r] in substring:
                    substring.remove(s[l])
                    l+=1
                substring.add(s[r])
                max_len=max(max_len,r-l+1)
        return max_len


        
