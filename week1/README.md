# Day 1 Challenge

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


## Mathematical context, real-world use, and realizations
This is the problem of **Two sum**, modelled by the equation a + b = T
In a typical transaction scenario, you might be asking which two actions explain a final state. For example, _Transactions = [+500, 200, 300, -5000]_. Notice that there are specific two conditions, +500 and -500 cancel out to give a final state of zero. 
The current solution works by brute force. There is an optimized solution that handles this without brute force.


# Day 2 Challenge
Given an integer array nums, find the subarray with the largest sum, and return its sum.

## Mathematical context and real-world use cases
Kadane's algorithm solves this in an optimized way. 

Here, a maximum sum is set, and a running sum is also set. We start adding numbers in the main array to the running sum. In each case, we check whether the running sum is greater than the maximum sum. If so, we assign the running sum value to the maximum sum. 

Otherwise, we ignore that iteration. After, we check whether the running sum runs into a negative. If it has, we bring it back to 0. This will ensure that anytime our sum is less than 0, we start from the next sum and ignore all previous sums. 

## Real-world use and its application in my weekend project
Kaldane's algorithm is the simplest dynamic-programming segmentation for neural time-series data.



# Day 3 Challenge
This is the Trionic Array 1 challenge on LeetCode

**Problem**
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:
nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.



# Day 4
**Problem**
You are given an integer array nums of length n.

A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

nums[l...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...r] is strictly increasing.
Return the maximum sum of any trionic subarray in nums.


# Day 5
You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

For each index i (where 0 <= i < nums.length), perform the following independent actions:
If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
If nums[i] == 0: Set result[i] to nums[i].
Return the new array result.

Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

##  The following systems make use of this simple pattern
CPUs sharing time across processes, Load balancing in distributed systems such as servers

# Day 6
This is a problem from GeeksForGeeks
You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
