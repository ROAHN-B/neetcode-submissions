class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = ["?", "!", "#", "$", "%", "^"]
        t = s.lower()
        string = "".join(t.split())
        output = []
        for ele in string:
            if ele in sc:
                output = list(string.replace(ele, ""))
            else:
                output.append(ele)
        reverse = output[::-1]

        if output == reverse:
            return True
        else:
            return False