# Contains Duplicate

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/contains-duplicate)

## Approach 1

"First sort the array and iterate the array and check its consecutive element is equal or not."

**Steps -**
> - First sort the array.
> - Iterate the array from beginning to end.
> - While iterating, check does i's element is equal to i+1's element, if yes return true else false.

```cpp
// Time Complexity - O(nlogn)             Space Complexity - O(1)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-1;i++){
            if(nums[i] == nums[i+1]) return true;
        }
        return false;
        
    }
};
```

## Approach 2

"Use map and check if frequency of any element is greater than 1 or not."

**Steps -**
> - Create map which stores element and its frequencies as a key-value pair respectively.
> - Now iterate the map and check the values, if any value is greater then 1, return true because we find that array contains duplicate else return false.

```cpp
// Time Complexity - O(n)             Space Complexity - O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> m;
        for(auto a:nums) m[a]++;
        for(auto a:m){
            if(a.second > 1) return true;
        }
        return false;
    }
};
```

## Approach 3

"Use set to store the elements, if size of set is not equal to size of array, depicts that array contains duplicates."

```cpp
// Time Complexity - O(n)             Space Complexity - O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for(auto i:nums) s.insert(i);
        if(nums.size()==s.size()) return false;
        return true;
        
    }
};
```

[Github](https://github.com/Hg03/)
