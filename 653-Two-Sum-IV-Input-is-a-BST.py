class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if k - node.val in hash_set:
                return True
            hash_set.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
