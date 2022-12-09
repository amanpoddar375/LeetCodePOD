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
    int find(TreeNode* root, int maxN, int minN){
        //base condition for leaf node i.e end of path
        if(root== NULL) return abs(maxN - minN);
        //updating the maxium and minimum value
        maxN = max(root->val, maxN);
        minN = min(root->val, minN);
        //for left traversal
        int left = find(root->left, maxN, minN);
        //for right traversal
        int right = find(root->right, maxN, minN);
        //returning the max value from different path
        return max(left, right);
    }
    int maxAncestorDiff(TreeNode* root) {
        if(root == NULL) return 0;
        return find(root, root->val, root->val);
    }
};
