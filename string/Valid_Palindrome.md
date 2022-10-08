# Valid Palindrome

**First solve by your own** [Visit problem](https://leetcode.com/problems/valid-palindrome/)

## Approach 

"We'll check the string using two pointers and check the characters are equal or not."

**Steps -**
> - Initialize two variables **left** (present at beginning of string) and **right** (present at end of string).
> - Iterate the string using left and right variables and check the below conditions.
> - Check if character is alphabet or numeric or not.
> - Check if string's left is equal to string's right or not. If it is equal, left++, right-- else string is not palindrome.

```cpp
// Time Complexity - O(logn)              Space Complexity - O(1)
class Solution {
public:
    bool isPalindrome(string s) {
        int size = s.size();
        int left = 0,right = size-1;
        while(left < right)
        {
            if(!isalnum(s[left])) left++;
            else if(!isalnum(s[right])) right--;
            else if(tolower(s[left])!=tolower(s[right])) return false;
            else
            {
                left++;
                right--;
            }
        }
        return true;
    }
};
```

[Github](https://github.com/Hg03/Grind75)