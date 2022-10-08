# Unique paths

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/unique-paths/)

## Approach 1

"In this, we'll recursively calculate the ways at each cell through traversing/visiting."

**Steps -**
> - We'll initialize i and j variable to traverse the matrix.
> - We'll check if i is equal to row - 1 and j is equal to column - 1, depicts we've reached the destination and that's our way so return 1.
> - We'll check if i and j are equal to row and column.
> - To reduce visiting cell more than once, store the result in dp.
> - Here we check if dp does not contains the way (mean does not equal to -1) return the way from dp.

```cpp
// Time Complexity - O(m x n)        Space Complexity - O(m x n)
class Solution {
public:
    int dfs(int i, int j, int m, int n, vector<vector<int>> &dp)
    {
        if(i==m || j==n){
            return 0;
        }
        if(i==m-1||j==n-1){
            return 1;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        return dp[i][j] = dfs(i+1,j,m,n,dp)+dfs(i,j+1,m,n,dp);
    }
    int uniquePaths(int m, int n)
    {
        vector<vector<int>> dp(m,vector<int>(n,-1));
        return dfs(0,0,m,n,dp);
    }
};
```

## Approach 2 

"Another approach is combinatorics approach."

**Refer this [video](https://youtu.be/t_f0nwwdg5o)**

```cpp
// Time Complexity - O(m-1) or O(n-1)        Space Complexity - O(1)
class Solution {
public:
    int uniquePaths(int m, int n)
    {
        int N = n + m -2;
        int r = m - 1;
        double res = 1;
        for(int i=1;i<=r;i++)
        {
            res = res * (N - r + i)/i;
        }
        
        return (int)res;
    }
};
```

[Github](https://github.com/Hg03/)