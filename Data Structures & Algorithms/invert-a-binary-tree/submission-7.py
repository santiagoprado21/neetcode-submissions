# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Considerar caso base que root este vacio
        if not root:
            return None
        #Invertir los primeros hijos de root
        root.left , root.right = root.right , root.left
        #Invertir izquierda 
        self.invertTree(root.left)
        #Invertir derecha
        self.invertTree(root.right)
        #Devolver el arbol
        return root