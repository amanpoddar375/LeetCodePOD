/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    void dfs(TreeNode* root, int low, int high){
        if(root == NULL) return;
        //addition of nodes which are within given range
        if(root->val >= low && root->val <= high){
            sum += root->val;
        }
        // for left traversal
        if(root->val > low) dfs(root->left, low, high);
        // for right traversal
        if(root->val < high) dfs(root->right, low, high);
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == NULL) return 0;
        dfs(root, low, high);
        return sum;
    }
};
