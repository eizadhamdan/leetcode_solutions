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
    int sumNumbers(TreeNode* root) {
        return sumPath(root, 0);   
    }

    int sumPath(TreeNode* node, int path) {
        if (node == nullptr) {
            return 0;
        }

        path = path * 10 + node->val;
        
        if (node->left == nullptr && node->right == nullptr) {
            return path;
        }

        return sumPath(node->left, path) + sumPath(node->right, path);
    }
};