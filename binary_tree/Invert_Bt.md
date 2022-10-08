# Invert Binary Tree

**First solve by your own** [Visit the problem](https://leetcode.com/problems/invert-binary-tree/)

## Approach


"Traverse the binary tree and swap the left and right of binary tree recursively"

**Steps -**
> - We'll performing postorder traversal in a binary tree.
> - The place where we process the node includes the swapping procedure.
> - Return the root at last.

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root!=nullptr)
        {
            invertTree(root->left);
            invertTree(root->right);
            TreeNode* temp = root->left;
            root->left = root->right;
            root->right = temp;
        }
        return root;
        
    }
};
```

[Github](https://github.com/Hg03/Grind75)