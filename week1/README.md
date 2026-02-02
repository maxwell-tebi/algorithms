# Day 1 Challenge

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


## Mathematical context, real-world use, and realizations
This is the problem of **Two sum**, modelled by the equation a + b = T
In a typical transaction scenario, you might be asking which two actions explain a final state. For example, _Transactions = [+500, 200, 300, -5000]_. Notice that there are specific two conditions, +500 and -500 cancel out to give a final state of zero. 
The current solution works by brute force. There is an optimized solution that handles this without brute force.


## Day 2 Challenge
Given an integer array nums, find the subarray with the largest sum, and return its sum.

## Mathematical context and real-world use cases
Kadane's algorithm solves this in an optimized way. 

Here, a maximum sum is set, and a running sum is also set. We start adding numbers in the main array to the running sum. In each case, we check whether the running sum is greater than the maximum sum. If so, we assign the running sum value to the maximum sum. 

Otherwise, we ignore that iteration. After, we check whether the running sum runs into a negative. If it has, we bring it back to 0. This will ensure that anytime our sum is less than 0, we start from the next sum and ignore all previous sums. 

## Real-world use and its application in my weekend project
Kaldane's algorithm is the simplest dynamic-programming segmentation for neural time-series data.
