class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<Integer>();
        for (int x : nums)
            s.add(x);
        return nums.length > s.size();
    }
}
