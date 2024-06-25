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
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;

        int fast_num = 0;
        int slow_num = 0;
        while (fast && fast->next) {
            fast = fast->next->next;
            fast_num += 2;
            slow = slow->next;
            slow_num++;

            if (fast == slow) {
                return fast;
            }
        }
        return nullptr;
    }
};