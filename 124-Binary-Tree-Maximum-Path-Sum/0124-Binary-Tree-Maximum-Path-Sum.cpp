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
    int result = INT_MIN;
    int find(TreeNode* root){
        // base condition to return leaf node
        if(root == NULL){
            return 0;
        }
        // if sum is -ve we return 0
        int left = max(0, find(root->left));
        int right = max(0, find(root->right));
        // updating the maximum sum till now
        result = max(result, root->val + left + right);
        //returning the maximum possible sum
        return root->val + max(left, right);
    }
    int maxPathSum(TreeNode* root) {
        find(root);
        return result;   
    }
};
