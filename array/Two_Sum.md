# Two Sum

**First solve by your own** [Visit problem](https://leetcode.com/problems/two-sum/)

## Brute Force approach

" Check for every possibilites in the array for two sum. "

**Steps -**
> - Use nested loops of 2 for loop and then iterate the array.
> - External loop iterate from beginning to end - 1 (i -> 0 to size - 2).
> - Internal loop iterate from beginning + 1 to end (j -> i+1 to size - 1).
> - Check array's i + array's j sum is found or not.

```cpp
// Time Complexity :- O(N^2)       Space Complexity :- O(1)
class Solution {
public:
   vector<int> twoSum(vector<int>& nums, int target) {
      int n = nums.size();
      for(int i=0;i<n;i++) {
          for(int j=i+1;j<n;j++) {
              if(nums[i] + nums[j] == target) return {i,j};
          }
      }
      return {1,-1};
   }
}
```

## Optimized approach 1 

" Use hash set for storing element and check the existence of target - element. "

**Steps -**
> - Iterate the array with a loop (i -> 0 to size - 1).
> - Check if target - array's i exists in array or not.
> - If it exists, we got our pair else store array's i in hash set.

```cpp
// Time complexity :- O(N)          Space Complexity :- O(N)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int,int> m;
        for(int i=0;i<n;i++) {
            int x = nums[i];
            int y = target - nums[i];
            if(m.find(y)!=m.end()) return {i,m[y]};
            m[nums[i]} = i;
        }
        return {1,-1};
    }
};
```

## Optimized Approach 2

"First we'll sort the array then use two pointer approach."

**Steps -**
> - First we'll sort the array.
> - We'll use two variables one(i) at beginnning and other(j) at ending of an array.
> - Now we check is the sum of number at ith and jth is equal to target or not.
> - If sum is lesser than target, we'll increment i.
> - If sum is greater than target, we'll decrement j.
> - Keep the process going on until i < j.

```cpp
// Time complexity :- O(NlogN)        Space Complexity :- O(N)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<pair<int, int>> v; // It is for storing the elements and its index position.
        for(int i=0;i<n;i++) v.push_back({nums[i],i});
        sort(v.begin(),v.end());
        int s=0,e = n-1;
        while(s<e)
        {
            int sum = v[s].first + v[e].first;
            if(sum == target) return {v[s].second,v[e].second};
            else if(sum>target) e--;
            else s++;
        }
        return {-1,-1};
    }
        
};
```

[GitHub](https://github.com/Hg03/Grind75)




