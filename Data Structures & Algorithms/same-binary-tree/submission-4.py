# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Ambos vacios
        if not p and not q:
            return True
        #Si uno de los dos esta vacio
        if not p or not q:
            return False
        #Si los valores son diferentes
        if p.val != q.val:
            return False
        return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)