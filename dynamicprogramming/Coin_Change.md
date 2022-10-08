# Coin Change 

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/coin-change/)

## Approach 1 

"We'll iterate from greater denomination coin to lowest to satisfy the amount to complete recursively. [Top-Down Approach]"

**Steps -**
> - We'll create a function which recursively the minimum coins to satisfy the amount.
> - If amount is 0, we dont need any coins so return 0.
> - If remainder or amount is less than 0, it would not be a valid case.
> - Then we'll iterate through coins and finds the minimum coins.

```cpp
// Time Complexity - O(amount * size(coins))           Space Complexity - O(amount * size(coins))
class Solution {
  public:
    int leastCoins(vector<int>& coins, int amount) {
      if (amount < 1) {
        return 0;
      }
      
      vector<int> dp(amount + 1);
      return coinChange(coins, amount, dp);
    }

  private:
    int coinChange(vector<int>& coins, int remainder, vector<int>& dp) {
      /*
        Minimum coins to make change for a negative amount is -1.
        This is just a base case we arbitrarily define.
      */
      if (remainder < 0) {
        return -1;
      }
    
      /*
        The minimum coins needed to make change for 0 is always 0
        coins no matter what coins we have.
      */
      if (remainder == 0) {
        return 0;
      }
  
      // We already have an answer cached. Return it.
      if (dp[remainder] != 0) {
        return dp[remainder];
      }
  
      /*
        No answer yet. Try each coin as the last coin in the change that
        we make for the amount
      */
      int minimum = INT_MAX;
      for (int coin: coins) {
        int changeResult = coinChange(coins, remainder - coin, dp);
  
        /*
          If making change was possible (changeResult >= 0) and 
          the change result beats our present minimum, add one to
          that smallest value
          
          We accept that coin as the last coin in our change making
          sequence up to this point since it minimizes the coins we
          need
        */
        if (changeResult >= 0 && changeResult < minimum) {
          minimum = 1 + changeResult;
        }
      }
  
      /*
        If no answer is found (minimum == max value) then the
        sub problem answer is just arbitrarily made to be -1, otherwise
        the sub problem's answer is "minimum"
      */
      dp[remainder] = (minimum == INT_MAX) ? -1 : minimum;
  
      return dp[remainder];
    }
};
```

## Approach 2

"In this, we create a dp array of size amount + 1, and check at every amount like (at 0 how much coins needed, at 1 how much and so on at amount 11 how much till the target). [Bottom-Up approach]"

**Steps -**
> - Create a vector dp of size amount + 1 and fill all the cells with value amount + 1.
> - dp[0] = 0.
> - Iterate the values from 1 till the amount.
> - Inside again iterate the coins and check which denominations of coins can we used to make the amount.
> - Then find minimum coins using the below formula.
> - Formula is - when we calculate the minimum value , we check the current indexed position - that position where that coins is used previously + 1.

```cpp
// Time Complexity - O(n^2)           Space Complexity - O(1)
class Solution {
  public:
    int leastCoins(vector<int>& coins, int amount) {
      // This table will store the answer to our sub problems
      vector<int> dp(amount + 1, amount + 1);
  
      /*
        The answer to making change with minimum coins for 0
        will always be 0 coins no matter what the coins we are
        given are
      */
      dp[0] = 0;
  
      // Solve every subproblem from 1 to amount
      for (int i = 1; i <= amount; i++) {
        // For each coin we are given
        for (int j = 0; j < coins.size(); j++) {
          // If it is less than or equal to the sub problem amount
          if (coins[j] <= i) {
            // Try it. See if it gives us a more optimal solution
            dp[i] = min(dp[i], dp[i - coins[j]] + 1);
          }
        }
      }
  
      /*
        dp[amount] has our answer. If we do not have an answer then dp[amount]
        will be amount + 1 and hence dp[amount] > amount will be true. We then
        return -1.
  
        Otherwise, dp[amount] holds the answer
      */
      return dp[amount] > amount ? -1 : dp[amount];
    }
};
```

[Github](https://github.com/Hg03/)
