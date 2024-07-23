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
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return;
        
        // Find the middle of the list
        ListNode* slow_ptr = head;
        ListNode* fast_ptr = head->next;
        
        while (fast_ptr != nullptr && fast_ptr->next != nullptr) {
            slow_ptr = slow_ptr->next;
            fast_ptr = fast_ptr->next->next;
        }
        
        // Now slow_ptr points to the middle node
        // Reverse the second half of the list
        ListNode* second = slow_ptr->next;
        slow_ptr->next = nullptr; // Cut off the first half
        
        ListNode* prev = nullptr;
        while (second != nullptr) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        
        // prev now points to the head of the reversed second half
        
        // Merge the two halves
        ListNode* first = head;
        second = prev;
        
        while (second != nullptr) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            
            first->next = second;
            second->next = temp1;
            
            first = temp1;
            second = temp2;
        }
    }
};