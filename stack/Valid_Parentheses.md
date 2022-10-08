# Valid Parentheses

**First solve by your own** [Visit problem](https://leetcode.com/problems/valid-parentheses/)

## Approach

**Steps -**
> - Create a stack for storing the characters to solve the problem.
> - Create a vector which stores open brackets and a map which open brackets as key and close brackets as values.
> - Iterate the expression and if we encounter
> - Open bracket, push it in stack.
> - Close bracket, compare map[stack's top] with character of expression. If equals, pop from stack, else expression is invalid.

```cpp
// Time Complexity - O(N)            Space Complexity - O(N)
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> bracketsMap = {{'(',')'},{'{','}'},{'[',']'}};
        vector<char> openBrackets{'(','{','['};
        vector<char> stack;
        for(char bracket : s)
        {
            if(find(openBrackets.begin(),openBrackets.end(),bracket)!=openBrackets.end()) stack.push_back(bracket);   
            else if(stack.size() > 0 && bracket == bracketsMap[stack.back()]) stack.pop_back();
            else return false;
        }
        return stack.size() == 0;
        
    }
};
```