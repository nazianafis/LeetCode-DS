class Solution:
    def __init__(self):
        self.out = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder(root)
        return self.out
    def postorder(self, root: Optional[TreeNode]) -> None:
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            if root.val is not None:
                self.out.append(root.val)
