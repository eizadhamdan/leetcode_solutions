/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* temp1 = head;
        ListNode* temp2 = head->next;
        ListNode* temp3 = temp2->next;
        head = temp2;
        int flag = 0;

        while (temp3 != nullptr) {
            temp2->next = temp1;
            temp1->next = temp3->next;
            temp2 = temp1->next;

            if (temp2 != nullptr) {
                temp1 = temp3;
                temp3 = temp2->next;
            }
            else {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            temp2->next = temp1;
            temp1->next = temp3;
        }
        else {
            temp1->next = temp3;
        }
        return head;
    }
};