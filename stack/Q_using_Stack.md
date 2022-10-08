# Implement Queue using Stacks

**First solve it by your own** [Visit the problem](https://leetcode.com/problems/implement-queue-using-stacks/)

## Approach 1
"We can modify push operation and rest should be same".

**Steps -**
> - Create two stack s1 and s2.
> - In case of push operation, pop the elements from s1 and push it in s2 until its empty and then push the elements which is given. Then again push all elements of s2 into s1 by popping until its empty.
> - In case of pop operation, simply pop from s1.
> - In case of peek, empty - return the top element and check the emptiness respectively.

```cpp
// Time Complexity - O(n)            Space Complexity - O(n)
class MyQueue {
public:
     stack<int> s1;
     stack<int> s2;
    MyQueue() {
        
    }
    
    void push(int x) {
        while(!s1.empty())
        {
            s2.push(s1.top());
            s1.pop();
        }
        s1.push(x);
        while(!s2.empty())
        {
            s1.push(s2.top());
            s2.pop();
        }
    }
    
    int pop() {
        int curr = s1.top();
        s1.pop();
        return curr;
    }
    
    int peek() {
        return s1.top();
    }
    
    bool empty() {
        return s1.empty();
    }
};
```

## Approach 2 

"We can modify pop operation and rest should be same"

**Steps -**
> - Simply create stacks s1 and s2 as before.
> - In case of push operation, simply push the given element in s1.
> - In case of pop operation, if s2 is not empty, return its top else push all elements of s1 in s2 through popping then return the top element of s2.
> - In case of peek, empty - return the top element and check the emptiness respectively.

```cpp
// Time Complexity - O(1) {amortised time complexity}       Space Complexity - O(n)
class MyQueue {
public:
    stack<int> s1;
    stack<int> s2;
    MyQueue() {
        
    }
    
    void push(int x) {
        s1.push(x);
    }
    
    int pop() {
        int curr;
        if(s2.empty())
        {
            while(!s1.empty())
            {
                s2.push(s1.top());
                s1.pop();
            }
        }
        curr = s2.top();
        s2.pop();
        return curr;
    }
    
    int peek() {
        if(s2.empty())
        {
            while(!s1.empty())
            {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }
    
    bool empty() {
        return s1.empty() and s2.empty();
    }
};

```

[Github](https://github.com/Hg03)
