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
    void inorderTraversal(TreeNode* root, int& temp) {
        if (!root) return;
        inorderTraversal(root->right, temp);
        root->val += temp;
        temp = root->val;
        inorderTraversal(root->left, temp);
    }
    TreeNode* bstToGst(TreeNode* root) {
        int temp = 0;
        inorderTraversal(root, temp);
        return root;
    }
};