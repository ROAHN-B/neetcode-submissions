# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        def height(root):
            if root is None:
                return 0
            left_depth=height(root.left)
            right_depth=height(root.right)

            if abs(left_depth-right_depth)>1:
                self.balanced=False
            
            return max(left_depth,right_depth)+1
        height(root)
        return self.balanced
