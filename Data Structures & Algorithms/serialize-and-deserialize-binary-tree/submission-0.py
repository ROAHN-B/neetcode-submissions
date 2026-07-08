# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(node):
            if node is None:
                res.append('N')
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tkn=data.split(',')
        index=0

        def build_tree():
            nonlocal index
            if index>=len(tkn):
                return None
            current=tkn[index]
            index+=1

            if current=='N':
                return None
            node=TreeNode(int(current))
            node.left=build_tree()
            node.right=build_tree()

            return  node
        return build_tree()


            
                
            

            


        