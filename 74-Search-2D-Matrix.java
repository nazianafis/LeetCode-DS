class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int arr[] : matrix)
            for(int i : arr)
                if (target == i)
                    return true;
        return false;
    }
}
