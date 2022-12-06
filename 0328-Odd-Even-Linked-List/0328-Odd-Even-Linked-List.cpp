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
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL || head->next == NULL || head->next->next == NULL)
            return head;
        ListNode* op = head;
        ListNode* ep = head->next;
        ListNode* startofep = head->next;
        while(op->next && ep->next){
            op->next = ep->next;
            ep->next = op->next->next;
            op = op->next;
            ep = ep->next;
        }
        op->next = startofep;
        return head;
    }
};
