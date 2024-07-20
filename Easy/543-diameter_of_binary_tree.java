/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        MaxLength max_length = new MaxLength();
        getDiameter(root, max_length);
        return max_length.val;
    }

    public int getDiameter(TreeNode node, MaxLength maxLength) {
        if (node == null) return 0;

        int left = getDiameter(node.left, maxLength);
        int right = getDiameter(node.right, maxLength);
        maxLength.val = Math.max(maxLength.val, left + right);

        return Math.max(left, right) + 1;
    }
}

class MaxLength {
    public int val = 0;
}