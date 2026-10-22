# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Considerar caso que el arbol este vacio
        if not root:
            return None
        #Invertir los primeros nodos
        root.left , root.right = root.right , root.left
        #Llamar invertTree a lado izquierdo
        self.invertTree(root.left)
        #Llamar invertTree a lado derecho
        self.invertTree(root.right)
        #Devolver Arbol (root)
        return root