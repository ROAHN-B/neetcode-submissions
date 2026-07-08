# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p,q):
            self.same=True
            if p is None and q is None:
                return self.same
            if p is None or q is None:
                self.same=False
                return self.same
            if p.val!=q.val:
                self.same=False
                return self.same
            
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)


            
        
