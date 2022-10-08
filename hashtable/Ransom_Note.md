# Ransom Note

**First solve it by your own** [Visit the problem](https://github.com/problems/ransom-note/)

## Approach

"Simply we store counts of character for magazine and then decrement the count for ransom note."

**Steps -**
> - Create an map which sotres the frequency of character for both strings.
> - First iterate the string 'magazine' and store the frequencies of characters.
> - Then iterate the string 'ransom note' and check is character exist in map if not return false, else decrement the count in map for character.

```cpp
// Time Complexity - O(n)            Space Complexity - O(n)
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> counts;
        for(char ch:magazine) counts[ch]++;
        for(char ch:ransomNote)
        {
            if(counts.find(ch) == counts.end()) return false;
            if(counts[ch] == 0)
                return false;
            counts[ch]--;
        }
        return true;
        
    }
};
```

[Github](https://github.com/Hg03/)
