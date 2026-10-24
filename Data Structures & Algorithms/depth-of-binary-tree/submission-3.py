# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Caso base es si root es none
        if not root:
            return 0
        #Sacar produndidad izquierda
        left_depth = self.maxDepth(root.left)
        #Sacar produndidad derecha 
        right_depth = self.maxDepth(root.right)
        #Devolver maxima
        max_depth = max(left_depth,right_depth)
        return 1+ max_depth