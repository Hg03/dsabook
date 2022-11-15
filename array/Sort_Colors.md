## Sort Colors

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/sort-colors/)

## Approach 1 

"Simply sort the array and then we can get the array in sorted fashion."

## Approach 2  (Dutch National Flag algorithm)

"We'll use three pointer and shift them according to the following conditions, and eventually sort the array."

**Steps -**

> - Initialize low with 0 and high with size of array - 1 and mid with 0.
> - Apply while loop until mid is less than equal to high.
> - If we get nums[mid] equals to 2, means we have to shift the 2 to last therefore swap high with mid, then decrement high.
> - If we get nums[mid] equals to 0, means we have to shift the 0 to beginning, therefore swap low with mid, then mid and low.
> - Else increment mid as usual.

```cpp
// Time Complexity - O(n)               Space Complexity - O(1)
class Solution {

public:

    void sortColors(vector<int>& nums) {

        int low=0,high=nums.size()-1,mid=0;

        while(mid<=high)

        {

            if(nums[mid]==2)

            {

                swap(nums[high],nums[mid]);

                high--;

            }

            else if(nums[mid]==0)

            {

                swap(nums[mid],nums[low]);

                mid=low+1;

                low++;

            }

           else

               mid++;

        }

        

    }

};
```

[Github](https://github.com/Hg03/)
