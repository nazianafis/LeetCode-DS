class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if ((r*c) != (mat.length*mat[0].length) || (r == mat.length && c == mat[0].length))
            return mat;
        
        int[][] newMat = new int[r][c];
        int i_old = 0;
        int j_old = 0;
        
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j ++){
                newMat[i][j] = mat[i_old][j_old];
                j_old ++;
                if (j_old == mat[i_old].length){
                    i_old ++;
                    j_old = 0;
                }
            }
        }
        
        return newMat;
    }
}
