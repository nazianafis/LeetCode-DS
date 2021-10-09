class Solution {
    public int maxProfit(int[] prices) {
        int max_prof = Integer.MIN_VALUE;
        int min_price = Integer.MAX_VALUE;
        for(int i : prices){
            min_price = Math.min(i, min_price);
            int curr_prof = i - min_price;
            max_prof = Math.max(curr_prof, max_prof);
        }
        return max_prof;
    }
}
