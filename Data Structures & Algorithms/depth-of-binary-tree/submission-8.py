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
        #Calcular la profundidad maxima izquierda y derecha
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        #Calcular la maxima, sumandole el primer nodo
        max_depth = max(left_depth,right_depth) + 1

        return max_depth