# Add binary

**First solve by your own** [Visit the problem](https://leetcode.com/problems/add-binary/)

## Approach

"As usual we add binary number, we'll perform the operation in reverse fashion"

**Steps -**
> - Keep two pointers at the last of both binary string.
> - Iterate both strings until i >= 0 and j >= 0.
> - When we encounter 1 and 1, carry is generated therefore keep tract of carry as well as answer.
> - After completion of iteration, reverse the answer and return it.

```cpp
// Time Complexity - O(n)           Space Complexity - O(n)
class Solution {
 public:
  string addBinary(string a, string b) {
    string ans;
    int carry = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;

    while (i >= 0 || j >= 0 || carry) {
      if (i >= 0)
        carry += a[i--] - '0';
      if (j >= 0)
        carry += b[j--] - '0';
      ans += carry % 2 + '0';
      carry /= 2;
    }

    reverse(begin(ans), end(ans));
    return ans;
  }
};
```

[Github](https://github.com/Hg03/Grind75)
