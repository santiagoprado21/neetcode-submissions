# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Considerar el caso base (Tree [])
        if not root:
            return None
        #Invetir los dos primeros hijos
        root.left , root.right = root.right , root.left
        #Invertimos los de la izquierda de forma recursiva
        self.invertTree(root.left)
        #Invertimos los de la derecha
        self.invertTree(root.right)
        return root

        #Tiempo : O(n) , Espacio : O(h) h: Altura del arbol