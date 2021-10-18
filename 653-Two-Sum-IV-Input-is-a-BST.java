class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> hashSet = new HashSet<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            TreeNode node = queue.remove();
            if(hashSet.contains(k - node.val))
                return true;
            hashSet.add(node.val);
            if(node.left != null)
                queue.add(node.left);
            if(node.right != null)
                queue.add(node.right);
        }
        return false;
    }
}
