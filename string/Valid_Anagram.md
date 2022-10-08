# Valid Anagram

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/valid-anagram/)

## Approach 1

"Simply sort both the strings and check their equality."

**Steps -**
> - First check the length of both strings, if length is not equal they can't be a valid anagram.
> - Sort both the strings and check they are equal or not.
> - If both are equal, return true else false.

```cpp
// Time Complexity - O(nlogn)          Space Complexity - O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()) return false;
        int n = s.size();
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if(s == t) return true;
        return false;
    }
};
```

## Approach 2

"We'll use a hashmap to keep the count of characters in both strings."

**Steps -**
> - First check the length of both strings, if they are not equal it can't be a valid anagram.
> - Iterate through both string in a loop, then increment the count for s1 string characters and decrement the count for s2 string characters.
> - Now check the map's each characters count, if any count is greater than 0, it is not a valid anagram else it is vaild anagram.

```cpp
// Time Complexity - O(n)         Space Complexity - O(n)
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> m;
        if(s.size()!=t.size()) return false;
        int n = s.size();
        for(int i=0;i<s.size();i++)
        {
            m[s[i]]++;
            m[t[i]]--;
        }
        for(auto it:m)
        {
            if(it.second) return false;
        }
        return true;
        
    }
};
```

[Github](https://github.com/Hg03/)