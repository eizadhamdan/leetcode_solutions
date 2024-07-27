/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        /*
        Copy the value of the next node into the current node and then 
        bypass the next node by adjusting the next pointer.
        */

        node->val = node->next->val;
        node->next = node->next->next;
    }
};
