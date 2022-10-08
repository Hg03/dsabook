# Lowest common ancestor of a binary search tree

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Approach 1 

"We'll find a path of each given node from root node and check the lists of path for finding the last common node."

**Steps -**
> - Create two vectors for storing the path of given node from root node.
> - Maintain one boolean for checking the presence of node's value in binary search tree.
> - Find the path with the help of rootToNode function (Practice [rootToNode problem]() also).
> - Now iterate both paths simultaneously and check the last common node which is the lowest common ancestor.

```cpp
// Time Complexity - O(n)        Space Complexity - O(n)
class Solution {
public:
     void rootToNode(TreeNode* root, TreeNode* target, vector<TreeNode*>& path, bool& found){
        // If tree is empty
        if(!root)return;        
        
        // Push the root node
        path.push_back(root);
         
        // If root is our target node
        if(root->val == target->val){
            found = true;
            return;
        }
        
        // Search further for target node
        if(!found)rootToNode(root->left, target, path, found);        
        if(!found)rootToNode(root->right, target, path, found);
         
        // If we didn't get the node's value, we'll pop the root node also from list
        if(!found){
            path.pop_back(); 
            return;
        }
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root)return root;
        
        vector<TreeNode*> Path_for_p;
        bool found = false;
        // Finding path for p from root node
        rootToNode(root, p, Path_for_p, found);
        
        vector<TreeNode*> Path_for_q;
        found = false;
        // Finding path for q from root node
        rootToNode(root, q, Path_for_q, found);
        

        TreeNode* lca = new TreeNode();
        int i = 0;
        // Checking the last common node that is eventually the lowest ancestor
        while(i<Path_for_p.size() && i<Path_for_q.size()){
            if(Path_for_p[i] != Path_for_q[i])break;
            lca = Path_for_p[i];
            i++;
        }
        return lca;
    }
};
```

## Approach 2

"Traverse the binary search tree and follow some conditions"

**Steps -**
> - While traversing, if we get value as one of the given node, return that node.
> - While traversing, if we get both node which are given return the root as that node is are lowest common ancestor.
> - From both side, if we get null and non null, return null, and if we get non null and non null, return root.

```cpp
// Time Complexity - O(n)                Space Complexity - O(1)
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL || root == p || root == q) return root;
        TreeNode* leftT = lowestCommonAncestor(root->left,p,q);
        TreeNode* rightT = lowestCommonAncestor(root->right,p,q);
        if(leftT == NULL) return rightT;
        else if(rightT == NULL) return leftT;
        else return root;
    }
};
```

[Github](https://github.com/Hg03/)



