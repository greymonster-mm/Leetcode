/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int v1, v2, carry,sum;
    v1 = v2 = carry = 0;
    struct ListNode* ret, * ret2, *tmp;
    int i = 0;
    ret = malloc(sizeof(struct ListNode));
    ret->next = NULL;
    ret2 = ret;
    while(l1 || l2 || carry)
    {
        v1 = l1 ? l1->val : 0;
        v2 = l2 ? l2->val : 0;
        sum = v1 + v2 + carry;
        carry = sum/10;

        if(i++ == 0)
        {
            ret->val = sum%10;
        }else
        {
            tmp = malloc(sizeof(struct ListNode));
            tmp->val = sum%10;
            tmp->next = NULL;
            ret->next = tmp;
            ret = ret->next;
        }    
        
        
        l1 = l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
    }
    return ret2;
}
