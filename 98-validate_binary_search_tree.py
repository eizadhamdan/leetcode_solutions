# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stck = [(root, float('-inf'), float('inf'))]

        while stck:
            node, minimum, maximum = stck.pop()

            if node.val <= minimum or node.val >= maximum:
                return False
            else:
                if node.left:
                    stck.append((node.left, minimum, node.val))

                if node.right:
                    stck.append((node.right, node.val, maximum))

        return True
        