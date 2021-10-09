class Solution {
    public int maxSubArray(int[] nums) {
        int local_max = 0;
        int global_max = Integer.MIN_VALUE;
        for(int i : nums){
            local_max = Math.max(i, (i + local_max));
            if(local_max > global_max)
                global_max = local_max;
        }
        return global_max;
    }
}
