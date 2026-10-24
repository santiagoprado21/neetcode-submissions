# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Ambos vacios (Verdadero porque son iguales)
        if not p and not q:
            return True
        #Uno de los dos es falso
        if not p or not q:
            return False
        #Cuando sus valores son diferentes
        if p.val != q.val:
            return False
        #Llamado recursivo comparando que izq y der sean true
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)