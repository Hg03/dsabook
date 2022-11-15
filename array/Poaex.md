## Product of Array Except Self

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/product-of-array-except-self/)

## Approach 1 

"We'll simply iterate for each element and calculate the product by leaving that element"

**Steps -**
> - Use nested for loops consist of two for loop.
> - In first for loop, initialize product so that we can store the product at every index position.
> - Inside second for loop, use if condition for neglecting the index for which we are calculating the product.
> - Then update the value with product's value in array.


```cpp
// Time Complexity - O(N^2)         Space Complexity - O(N)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res;
        for(int i=0;i<n;i++)
        {
            int product = 1;
            for(int j=0;j<n;j++)
            {
                if(i == j) continue;
                else product*=nums[j];
            }
            res.push_back(product);
        }
        return res;
    }
};
```

## Approach 2 

"In this, we'll create two array, one will calculate the product from left and another from right."

**Steps -**

> - First create two array of same size as given array named as cumulativeFromLeft and cumulativeFromRight.
> - In cumulativeFromLeft and cumulativeFromRight, assign initial and final value to be 1 respectively.
> - Use one for loop, and fill the values in cumulativeFromLeft array by having product of their immediate previous values from given array and cumulativeFromLeft array.
> - Then use another for loop, and fill the values in cumulativeFromRight array by having product of their immediate previous values from given array and cumulativeFromRight array.
> - Now multiple both array with their corresponding element, and we got our result.

```cpp
// Time Complexity - O(N)          Space Complexity - O(1)
class Solution {
public:
    vector<int> productExceptSelf(vector<int> nums){
          int n = nums.size();
          int cumulativeFromLeft[n];
          cumulativeFromLeft[0] = 1;
          for(int i = 1; i < n; i++)
            cumulativeFromLeft[i] = cumulativeFromLeft[i-1] * nums[i-1];

          int cumulativeFromRight[n];
          cumulativeFromRight[n-1] = 1;
          for(int i = n-2; i >= 0; i--)
            cumulativeFromRight[i] = cumulativeFromRight[i+1] * nums[i+1];

          vector<int> output;
          for(int i = 0; i < n; i++)
            output.push_back(cumulativeFromLeft[i] * cumulativeFromRight[i]);

          return output;
    }
};
```
[Github](https://github.com/Hg03/)
