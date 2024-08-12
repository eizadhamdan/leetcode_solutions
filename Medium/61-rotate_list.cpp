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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k == 0) {
            return head;
        }
        
        int num = 1;
        ListNode* ptr = head;
        while (ptr->next) {
            num++;
            ptr = ptr->next;
        }
        k = k % num;
        if (k == 0) return head;
        ptr->next = head;
        ListNode* temp = head;
        for (int i = 1; i < num - k; i++) {
            temp = temp->next;
        }
        ListNode* new_head = temp->next;
        temp->next = nullptr;
        return new_head;
    }
};