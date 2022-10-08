# Balanced Binary Tree

**First solve it by your own** [Visit the problem](https://leetcode.com/balanced-binary-tree/)

## Approach 1 

"Check the left height, right height of binary tree for every node and check if are they balanced or not."

**Steps -**
> - First check isn't the root is null, if yes return -1.
> - Now calculate the left height and right height of a binary tree recursively.
> - Check the balanced nature at every node i.e. abs(left_height - right_height) <= 1.

```cpp
// Time Complexity - O(N)           Space Complexity - O(h)
class Solution {
public:
    int height(TreeNode* root){
        if(!root)
            return -1;
        int leftheight = height(root->left);
        int rightheight = height(root->right);
        return max(leftheight,rightheight) + 1;
        }
      
    bool isBalanced(TreeNode* root){
        if(root == NULL) return true;
        int lefth = height(root->left);
        int righth = height(root->right);
        return abs(lefth - righth) <=1 && isBalanced(root->left) && isBalanced(root->right);
    }
};
```

## Approach 2 

"In previous approach, we are visiting nodes repeatedly, so try to store previous results."

```cpp
// Time Complexity - O(N)              Space Complexity - O(h)
class Solution {
public:
    bool ans;
    int checkBalance(TreeNode* root){
        if(!root)
            return 0;
        if(!ans) // if Answer is already False then return it.
            return 0;
        int leftSubTree = checkBalance(root->left);
        int rightSubTree = checkBalance(root->right);
        if(abs(leftSubTree-rightSubTree) > 1){
            ans = false;
        }
        return 1 + max(leftSubTree, rightSubTree);
    }
    bool isBalanced(TreeNode* root){
        ans = true;
        int temp = checkBalance(root);
        return ans;
    }
};
```

[Github](https://github.com/Hg03)
