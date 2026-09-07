class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
               
                skip_left = check_palindrome(s, l + 1, r)
                skip_right = check_palindrome(s, l, r - 1)
                
                return skip_left or skip_right
            
         
            l += 1
            r -= 1
            
        return True