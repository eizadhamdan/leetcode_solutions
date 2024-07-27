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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* ptr1 = list1;
        ListNode* prevA = nullptr;

        for (int i = 0; i < a; i++) {
            prevA = ptr1;
            ptr1 = ptr1->next;
        }

        ListNode* ptr2 = ptr1;

        for (int i = a; i <= b; i++) {
            ptr2 = ptr2->next;
        }

        prevA->next = list2;
        ListNode* ptr3 = list2;

        if (ptr3 != nullptr) {
            while (ptr3->next != nullptr) {
                ptr3 = ptr3->next;
            }
            ptr3->next = ptr2;
        }

        return list1;
    }
};
