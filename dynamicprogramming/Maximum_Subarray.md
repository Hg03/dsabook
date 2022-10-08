# Maximum subarray

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/maximum-subarray/)

## Approach 1

"Simply iterate through each subarray and calculate its maximum sum."

**Steps -**
> - Initialize sum variable to calculate sum of each subarray.
> - Initialize maximumm sum variable to keep tract of maximum sum of particular subarray.
> - Use nested loop of two for loop, external iterates from i -> 0 to size - 1 and internal from j -> i to size - 1.
> - Keep track of sum and maximum sum.

```cpp
// Time Complexity - O(n^2)          Space Complexity - O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int maxSum = 0;
        for(int i=0;i<n;i++)
        {
            int sum = 0;
            for(int j=i;j<n;j++)
            {
                sum+=nums[j];
                maxSum = max(maxSum,sum);
            }
        
        }
        return maxSum;
    }
};
```

## Approach 2 (Kadane's algorithm)

"Traverse the array once and keep track of max sum neglecting negative sum."

**Steps -**
> - Traverse the array with 1 for loop.
> - Initialize maximum sum variable and sum variable as discussed above.
> - In for loop, is the maximum sum is enough or by adding next element makes the sum more greater.
> - If sum is less than 0, initialize sum variable with 0.

```cpp
// Time complexity - O(n)      Space Complexity - O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        int maxSum = INT_MIN;
        for(int i=0;i<n;i++)
        {
            sum+=nums[i];
            maxSum = max(maxSum,sum);
            if(sum < 0) sum = 0;
        }
        return maxSum;
    }
};

```

[Github](https://github.com/Hg03/)
