# Merge 2 Sorted Linked List

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/merge-two-sorted-lists)

## Approach

"Traverse both linked list correspondingly and compare the values of nodes"

**Steps -**
> - Initialize two pointers i.e. ans (for storing the answer) and tail (for maintaining the tail of a list).
> - First check the header's value of both lists, assign node to answer having lesser value.
> - Then iterate both list until one of them are not exhausted.
> - Move the lists next to next and maintain tail and answer list.
> - If one of the list is exhausted, assign the remaining list at the end.



```cpp
// Time Complexity - O(m+n)         Space Complexity - O(1)
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL) return list2;
        if(list2 == NULL) return list1;
        ListNode *ans, *tail;
        // Decide head for the resulted linked list
        if(list1->val < list2->val)
        {
            ans = list1;
            tail = list1;
            list1 = list1->next;
        }
        else
        {
            ans = list2;
            tail = list2;
            list2 = list2->next;
        }
        
        // Traverse further
        while(list1 && list2)
        {
            if(list1->val < list2->val)
            {
                tail->next = list1;
                tail = list1;
                list1 = list1->next;
            }
            else
            {
                tail->next = list2;
                tail = list2;
                list2 = list2->next;
            }
        }
        
        // Merging remaining linked list
        if(!list1) tail->next = list2;
        else tail->next = list1;
        
        return ans;
    }
};
```

[Github](https://github.com/Hg03/)