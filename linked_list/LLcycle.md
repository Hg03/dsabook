# Detect cycle in linked list

**First solve by your own** [Visit problem](https://leetcode.com/problems/linked-list-cycle/)

## Brute force approach

**Steps -**
> - Create a hash set which stores values of the nodes of linked list.
> - Iterate the linked list and check that does that node's value exist in hash set or not.
> - If node's value exist in hash set, depicts that cycle is present in linked list else insert node's values into hash set.

```cpp
// Time Complexity - O(n)           Space Complexity - O(n)
class Solution {
public:
    bool hasCycle(ListNode *head) {
         unordered_set<ListNode*> s;
         while(head!=NULL)
         {
             if(s.find(head) != s.end()) return true;
             s.insert(head);
             head = head->next;
         }
         return false;
    }
};
```

## Optimized Approach

"Using slow and fast pointer"

**Steps -**
> - Create two pointer named slow and fast.
> - Slow pointer moves one node at a time and fast pointer moves two nodes at a time.
> - Iterate the linked list using both pointer.
> - If at an instance, slow pointer equals to fast, depicts that cycle is present in linked list else cycle is absent.

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
          ListNode* slow = head;
          ListNode* fast = head;
          while(fast != NULL && fast->next != NULL)
          {
              slow = slow->next;
              fast = fast->next->next;
              if(slow == fast) return true;
          }
          return false;
    }
};
```

[GitHub](https://github.com/Hg03/Grind75)