class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posdiag=set()
        nesdiag=set()
        res=[]
        board=[["."]*n for i  in range(n)]

        def backtrack(r):
            if r==n:
                copy=["".join(row)for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in nesdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                nesdiag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                nesdiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
