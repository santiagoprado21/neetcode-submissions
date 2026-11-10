# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode])-> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) ->   bool:
        #Comprobar si root es vacio
        if not root:
            return False
        #Comprobar si subroot es vacio
        if not subRoot:
            return True
        #Comprobar que root y subroot no sean el mismo arbol
        if self.isSameTree(root,subRoot):
            return True
        #Recursivo para ver si en algun nodo de root es igual a subtree
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        


        
        