# Containers with most water

**First solve by your own** [Visit the problem](https://leetcode.com/problems/container-with-most-water/)

## Approach 1

"Simply explore every pair of heights and calculate its area and keep tracking of max area."

**Steps -**
> - Initialize two variables i and j.
> - i iterates from beginning to end and j iterates from i + 1 to end.
> - Calculate the area while looping.

```cpp
// Time Complexity - O(n^2)            Space Complexity - O(1)
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = INT_MIN;
        for(int i=0;i<height.size();i++)
        {
            for(int j=i+1;j<height.size();j++)
            {
                maxArea = max(maxArea, min(height[i],height[j])*(j-i));
            }
        }
        return maxArea;
    }
};
```

## Approach 2

"Try to attack from both sides of array"

**Steps -**
> - Initialize two variables i and j.
> - i iterates from beginning and j iterates from end.
> - Loop until i < j.
> - Calculate the area while looping.

```cpp
// Time Complexity - O(logn)            Space Complexity - O(1)
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int area;
        int maxArea = INT_MIN;
        while(left < right)
        {
            area = min(height[left],height[right]) * (right-left);
            maxArea = max(maxArea,area);
            if(height[left] < height[right]) left++;
            else right--;
        }
        return maxArea;
    }
};
```

[Github](https://github.com/Hg03)