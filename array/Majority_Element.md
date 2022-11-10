## Majority Element

**First solve by your own** [Visit problem](https://leetcode.com/problems/majority-element/)

## Approach 1 

"Iterate the array with nested loops consist of 2 loops and check frequency of each element individually."

**Steps -**
> - Initialize the majorityCount variable to which we compare the frequency of other element.
> - Iterate the array (with 2 loops), one for fixing the element and other for calculating the count of that fixed element.
> - Now we check is that fixed element's frequency is greater than majorityCount or not.

```cpp
// Time Complexity - O(n^2)            Space Complexity - O(1)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majorityCount = nums.size()/2;
        for(int num : nums)
        {
            int count = 0;
            for(int elem : nums)
            {
                if(elem == num)
                    count++;
            }
            if(count > majorityCount)
                return num;
        }
        return -1;
    }
};
```

## Approach 2 

"We'll use hashmap to store element and its frequency as a key value respectively and check its values."

**Step -**
> - Create a hashmap which stores a elements as a key and its frequency as a value.
> - Iterate through the hashmap and compare its value with nums.size()/2.

```cpp
Time Complexity - O(NlogN)      Space Complexity - O(N)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
       
       unordered_map<int,int> m;
       for(int i=0;i<nums.size();i++) m[nums[i]]++;
       for(auto i:m)
       {
           if(i.second > nums.size()/2) return i.first;
       }
       return 0;
        
        
    }
};
```

## Moore's Voting algorithm

"This algorithm works on the fact that if an element occurs more than N/2 times, it means that the remaining elements other than this would definitely be less than N/2. So let us check the proceeding of the algorithm."


**Steps -**
> - Select a candidate (any value) and initialize vote variable which counts the frequency.
> - While iterate, if number is equal to the candidate, increment the vote else decrement the vote.
> - If vote is equals to 0, change the candidate.

```cpp
// Time Complexity - O(n)         Space Complexity - O(1)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Moore voting algorithm
        int votes = 0;
        int candidate = 0;
        for(int num : nums)
        {
            if(votes == 0) candidate = num;
            if(num == candidate) votes++;
            else votes--;
        }
        return candidate;
    }
};
```
[Github](https://github.com/Hg03)
