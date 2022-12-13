class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        for(int i = 1; i<matrix.size();i++)
            for(int j = 0;j<matrix[0].size(); j++)
                if (j == 0)
                    matrix[i][j] = min((matrix[i][j] + matrix[i-1][j]), (matrix[i][j] + matrix[i-1][j+1]));
                else if(j == matrix[0].size()-1)
                    matrix[i][j] = min((matrix[i][j] + matrix[i-1][j]), (matrix[i][j] + matrix[i-1][j-1]));
                else
                    matrix[i][j] = matrix[i][j]+min(matrix[i-1][j],min(matrix[i-1][j+1],matrix[i-1][j-1]));
        return *min_element(matrix[matrix.size()-1].begin(),matrix[matrix.size()-1].end());
    }
};
