# Insert Interval

**First solve it by our own** [Visit the problem](https://leetcode.com/problems/insert-intervals/)

## Approach

" Here, we iterate each intervals and check the intervals with new interval given and then as according we'll merge/update it."

**Steps -**
> - First check does that interval exist in beginning or not.
> - Iterate the interval using i.
> - Then check if current interval's second value is lesser than newInterval's first value, if yes current intervals should be placed first in the result vector.(Condition for non-overlapping)
> - Now check if current interval's first value is lesser than newInterval's second value, if yes update newInterval as its first value is minimum of current and new Interval's first value and its second value is maximum of both interval's second value.
> - Then push it in result vector.
> - After all the merging and overlapping finished, push all the remaining intervals in results.

```cpp
// Time Complexity - O(n)            Space Complexity - O(n)
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int i = 0;
        int n = intervals.size();
        
        vector<vector<int>> result;
        
        // If current interval's second value is lesser than newInterval's first value, current interval would be the initial interval so push it.
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }
        
        // Updating the new interval state
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);
        
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }
        
        return result;
    }
};
```
[Github](https://github.com/Hg03/)
