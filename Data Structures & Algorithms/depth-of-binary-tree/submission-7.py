# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Caso base, root []
        if not root:
            return 0
        #Calcular depth de cada lado
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        #Calcular el maximo (Con nodo incial)
        max_depth = max(left_depth,right_depth) + 1
        #Devolver el maximo
        return max_depth