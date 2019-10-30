# Competitive Programming

## Motivation

Competitive programming combines two topics:

1.  The *design* of algorithms

    Requires problem-solving skills and mathematical thinking. The designed algorithm has to be correct and efficient. Theoretical knowledge of algorithms is important as a solution is typically a combination of well-known techniques and new insights.

2.  The *implementation* of algorithms

    Requires good programming skills. Just knowing the idea of the solution is not enough, the implementation has to be precise. Typically, time is of the essence and writing the code should not take too long.

Competitive programming has many benefits:

*   Enhances problem-solving skills.
*   Prepares you well for technical interviews.
*   Helps you not just learn the fundamentals but actually implement.
*   Collaborating in a team of programmers.
*   It's fun!

## Time Complexity

The time complexity of an algorithm estimates how much time the algorithm will use for some input. The efficiency of algorithms is important in competitive programming. Generally, it is easy to design an algorithm that solves the problem slowly but it's challenging to write a fast algorithm. By calculating the time complexity, we can check whether our algorithm is fast enough without actually implementing it.

The time complexity is denoted using _O(...)_ where the 3 dots represent some function. Usually, the variable _n_ denotes the input size. For example, if the input is a `list` of numbers, _n_ will be the length of the `list`.

Complexity classes:

O(1) constant < O(log n) logarithmic < O(n) < linear < O(n log n) linearithmic < O(n²) quadratic < O(n³) cubic < O(2ⁿ) exponential < O(n!) factorial

Most sites these days allow 10⁸ operations per second, only a few sites still allow 10⁷ operations.

![](assets/complexity-chart.jpeg)

| Input Size | Required Time Complexity |
|:----------:|:------------------------:|
| n ≤ 10    | O(n!) |
| n ≤ 20    | O(2ⁿ) |
| n ≤ 500   | O(n³) |
| n ≤ 5000	| O(n²) |
| n ≤ 10⁶	| O(n log n)
| n ≤ 10⁸	| O(n) |
| n is large | O(1) or O(log n) |

## Climbing Stairs

Read the [problem statement](https://leetcode.com/problems/climbing-stairs/).

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        f0, f1 = 0, 1
        for i in range(n):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2
```

## 2Sum

Read the [problem statement](https://leetcode.com/problems/two-sum/).

### Brute Force

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]
```

### Sort List

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        nums[i] = [nums[i], i]
    nums.sort()
    low = 0
    high = len(nums) - 1
    while low < high:
        sum = nums[low][0] + nums[high][0]
        if sum == target:
            return [nums[low][1], nums[high][1]]
        elif sum < target:
            low += 1
        else:
            high -= 1
```

### Dictionary

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    map = dict()
    for i in range(len(nums)):
        complement = target - nums[i] 
        if complement in map:
            return [i, map[complement]]
        else:
            map[nums[i]] = i
```

[3Sum](https://leetcode.com/problems/3sum/) is a variation to this problem.

## Majority Element

Read the [problem statement](https://leetcode.com/problems/majority-element/).

### Sort List

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
```

### Dictionary

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = dict()

        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > len(nums) / 2:
                return num
```

### Boyer-Moore Algorithm

```python
def majorityElement(self, nums: List[int]) -> int:
    counter = 0

    for num in nums:
        if counter == 0:
            m = num
        if m == num:
            counter += 1
        else:
            counter -= 1
    
    return m
```

[Majority Element II](https://leetcode.com/problems/majority-element-ii/) is a variation to this problem.

## Longest Substring Without Repeating Characters

Read the [problem statement](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    map = dict()
    length = low = high = 0

    for i in range(len(s)):
        char = s[i]
        if char in map:
            low = max(map[char] + 1, low)
        map[char] = i
        length = max(high - low + 1, length)
        high += 1
    
    return length
```

## Practice

There are plenty of platforms for you to practice:

*   [HackerRank](https://hackerrank.com)
*   [CodeForces](http://codeforces.com)
*   [SPOJ](https://www.spoj.com/)
*   [LeetCode](http://leetcode.com)
*   [CodeChef](http://codechef.com)
*   [TopCoder](https://www.topcoder.com/)
*   [HackerEarth](https://www.hackerearth.com/)

## Summary

We covered:

*   [Motivation](#motivation)
*   [Climbing Stairs](#climbing-stairs)
*   [2Sum](#2sum)
*	[Majority Element](#majority-element)
*	[Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)
*   [Practice](#practice)