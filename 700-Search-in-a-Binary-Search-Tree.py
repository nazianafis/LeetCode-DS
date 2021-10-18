class Solution:

# recursive solution
#    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#        if not root:
#            return None
#        if root.val == val:
#            return root
#        if val < root.val:
#            return self.searchBST(root.left, val)
#        if val > root.val:
#            return self.searchBST(root.right, val)

# iterative solution        
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root 
