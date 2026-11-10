# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Caso base root vacio
        if not root:
            return None
        #Invertimos los primeros hijos de root
        root.left,root.right = root.right,root.left
        #Aplicamos recursion tanto para los hijos izquierdos como derechos
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root