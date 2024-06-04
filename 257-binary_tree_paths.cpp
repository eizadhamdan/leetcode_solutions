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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        if (root == nullptr) {
            return result;
        }
        string current_path = to_string(root->val);
        if (root->left == nullptr && root->right == nullptr) {
            result.push_back(current_path);
        }
        if (root->left != nullptr) {
            dfs(root->left, current_path, result);
        }
        if (root->right != nullptr) {
            dfs(root->right, current_path, result);
        }


        return result;
    }
    void dfs(TreeNode* node, string current_path, vector<string>& result) {
        current_path += "->";
        current_path += to_string(node->val);

        if (node->left == nullptr && node->right == nullptr) {
            result.push_back(current_path);
            return;
        }
        if (node->left != nullptr) {
            dfs(node->left, current_path, result);
        }
        if (node->right != nullptr) {
            dfs(node->right, current_path, result);
        }
    }
};