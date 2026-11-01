# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,low,high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (
                validate(node.left,low,node.val) and
                validate(node.right,node.val,high)
            )
        return validate(root,float("-inf"),float("inf"))

        #Caso base root vacio (node porque se define root abajo)
        #Caso en que no se cumplen los limites, sub arboles invalidos
        #Caso node.left se actualiza el high
        #Caso node.right se actualiza el low
        #Return validate(root,-infinito,infinito)