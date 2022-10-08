# Climbing Stairs

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/climbing-stairs/)

## Approach 1 

"We'll simply find all possible ways from nth step to 0th step recursively."

**Steps -**
> - Check if steps become 0, depicts we are at the destination , so return 1.
> - Now iterate through steps i.e. 1 and 2 and call the function for total_steps - 1 and total_steps - 2 and calculate the total ways.

```cpp
// Time Complexity  O(m^n) where n is the number of steps and m is the size of possibleSteps     Space Complexity - O(n)
class Solution {
public:
    int climbStairs(int n) {
        vector<int> possibleSteps = {1,2};
        return numberOfWays(n,possibleSteps);
    }
    
    int numberOfWays(int n,vector<int>& possibleSteps){
        if(n==0) return 1;
        int nbWays = 0;
        for(int steps:possibleSteps)
        {
            if(n-steps >= 0)
                nbWays+=numberOfWays(n-steps,possibleSteps);
        }
        return nbWays;
    }
};
```

## Approach 2

"We'll create a new vector and fill the values which depicts the number of ways at that steps."

**Steps -**
> - Create a vector of size n+1, and assign 1 to first position of newly created vector.
> - Then add the values at indexed position - steps (one by one) if exist, and assign at the index.
> - At the last index, we'll get a possible ways to climb stairs.

```cpp
// Time Complexity - O(n^2)           Space Complexity - O(n)
class Solution {
public:
    int climbStairs(int n) {
        vector<int> possibleSteps = {1,2};
        return numberOfWays(n,possibleSteps);
    }
    
    int numberOfWays(int n,vector<int>& possibleSteps){
        int waysArray[n+1];
        waysArray[0] = 1;
        for(int i=1;i<n+1;i++)
        {
            int ways = 0;
            for(int step : possibleSteps)
            {
                if(i-step >= 0) ways += waysArray[i-step];
                
            }
            waysArray[i] = ways;
        }
        return waysArray[n];
    }
};
```

[Github](https://github.com/Hg03/)
