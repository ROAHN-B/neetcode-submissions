class Solution:
    def isHappy(self, n: int) -> bool:
        sum=set()
        while n!=1:
            if n in sum:
                return False
            sum.add(n)
            res=0
            for i in str(n):
                res+=int(i)**2
            n=res
        return True