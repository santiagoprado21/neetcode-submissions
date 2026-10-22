# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Caso base cuando root este vacio
        if not root:
            return 0
        #Calcular el maximo entre ambos hijos
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        max_depth = 1 + max(left_depth,right_depth)
        #Devolver la profundidad
        return max_depth
        