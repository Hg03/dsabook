# Validate Binary Search Tree 

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/validate-binary-search-tree/)

## Brute Force Approach 

"Traverse the tree and check is root's left is smaller than root or not as well for root's right."

**Steps -**
> - First check isn't the root is null ,it depicts tree is empty and return true.
> - Check if root's left value is greater than root or root's right value is smaller than root. If it is , binary search tree is invalid.
> - Now traverse the left subtree and right subtree and check the same.

```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if(root) return true;
        
        if(root -> left && root->left > root) return false;
        if(root -> right && root->right < root) return true;
        
        return isValidBST(root->left) && isValidBST(root->right);
    }
};
```

**But but but !!! , This one is kinda wrong approach, it doesn't solve each test case**
> - Every time value is only checked by its closest ancestor, means values also has to be small or greater than its grand-grand root node also.
> - For this, we have to be clear about the range to check the value for.


## Optimized Approach

"We'll use minimum and maximum value constraints for comparing the values of left and right node."

**Steps -**
> - Check first that isn't the root is null.
> - Initialize the minimum and maximum value to be -infinity and infinity.
> - Check if root's value is greater than minimum value and lesser than maximum value.
> - Update the minimum and maximum value as we traverse to left and right subtree.

Example 
![Valid BST](https://i0.wp.com/algorithms.tutorialhorizon.com/files/2014/09/IsBST-Min-Max.png)

```cpp
//Time Complexity - O(N)        Space Complexity - O(h) where h is the height of the BST.
class Solution {
public:
    bool checkValidBST(TreeNode* root, long min, long max){
        if(root == NULL) {
            return true;
        }

        if(root->val <= min || root->val >= max) {
            return false;
        }

        return checkValidBST(root->left, min, root->val) && checkValidBST(root->right, root->val, max);
    }
    bool isValidBST(TreeNode* root){
      if(root == NULL)
        return true;
        return checkValidBST(root, LONG_MIN, LONG_MAX);
    }
};
```
[Github](https://github.com/Hg03/)