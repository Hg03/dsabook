# 3 sum

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/3sum/)

## Approach 1 
"Simply we'll use nested loops consist of 3 loops and check the sum is equal to target or not. [TLEd solution]"
**Time Complexity - O(n^3),            Space Complexity - O(n)**

## Approach 2
"We'll fix one value and apply two pointer approach in rest of the array."

**For e.g. we need to find a,b,c number which sums upto 0 (or if any target is given), we'll choose a for an instance and check the other two b and c such that b + c = -a, if we found it we got our triplet**

**Steps -**
> - First sort the array.
> - We are using one for loop ,and inside it we are using while loop for two pointer approach.
> - For loop (runs from i -> 0 to n-1) fixes a number then inside we'll initialize two pointer start (i+1) and end (n-1).
> - Now we'll check if sum of value at start position and end position is equal to negative of value at ith position. If yes, we got our triplet. Store the triplet.

```cpp
// Time Complexity - O(n^2)            Space Complexity - O(1)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
      vector<vector<int>> output;
      sort(nums.begin(), nums.end());
      for(int i=0;i<nums.size();i++)
      {
          int a = nums[i];
          int other2 = -a;
          int s = i+1;
          int e = nums.size()-1;
          while(s<e)
          {
              if(nums[s] + nums[e] == other2)
              {
                  output.push_back({nums[i],nums[s],nums[e]});
                  while(s<e && nums[s] == nums[s+1]) s++; // If previous element is same as current element
                  while(s<e && nums[e] == nums[e-1]) e--; 
                  s++;
                  e--;
              }
              else if(nums[s] + nums[e] < other2) s++;
              else e--;
          }
          while(i+1 < nums.size() && nums[i] == nums[i+1]) i++;
      }
      return output;
    }



};
```

[Github](https://github.com/Hg03/)



