# Best Time to Buy and sell stocks

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Approach 1

"We'll iterate to each possibility and calculate the max of difference between elements."

**Steps -**

> - Initialize a variable maxProfit with INT_MIN which stores the maximum profit we'll get.
> - Iterate array with nested loops (of 2 loops), external loop(i) will iterate from 0 to size of array - 1 and internal loop(j) will iterate from i + 1 to size.
> - Then we'll calculate the maxProfit of difference between prices[j] - prices[i].

```cpp
// Time Complexity - O(n^2)      Space Complexity - O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        for(int i=0;i<prices.size()-1;i++)
        {
            for(int j=i+1;j<prices.size();j++)
            {
                maxProfit = max(maxProfit,prices[j]-prices[i]);
            }
        }
        return maxProfit;
    }
};
```

## Optimized Approach

"We'll keep track of the minimum value from starting of the array and iterate the values further and calculate the difference as well as maximum profit."

**Steps -**
> - Initialize minPrice which store the minimum price on which we should buy the stocks and maxProfit to calculate the maximum profit.
> - Iterate the array with a for loop(1 to n).
> - Keep track of the minimum price.
> - Calculate the max of difference between current price and minimum price.

```cpp
// Time Complexity - O(n)          Space Complexity - O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxPro = 0;
        for(int i = 0;i<prices.size();i++){
            minPrice = min(minPrice,prices[i]);
            maxPro = max(maxPro,prices[i] - minPrice);
        }
        return maxPro;
    }
};
```

[Github](https://github.com/Hg03/)
