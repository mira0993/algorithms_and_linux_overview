# Analysis of Algorithms



## Contents
- [Constant Function](#constant-function)
- [Logarithm Function](#logarithm-function)
- [Linear Function](#linear-function)
- [N-log-N Function](#n-log-n-function)
- [Quadratic Function](#quadratic-function)
- [Cubic Function](#cubic-function)
- [Exponential Function](#exponential-function)



## Constant Function
`O(c)`

The constant function is useful in algorithm analysis, because it characterizes the number of steps needed to do a basic operation on a computer, like adding two numbers, assigning a value to some variable, or comparing two numbers.

## Logarithm Function
`O(log n)`

The most common base for the logarithm function in computer science is 2, as computers store integers in binary, and because a common operation in many algorithms is to repeatedly divide an input in half. In fact, this base is so common
that we will typically omit it from the notation when it is 2.

We can easily compute the smallest integer greater than or equal to log<sub>b</sub> n. For positive integer, n, this value is equal to the number of times we can divide n by b before we get a number less than or equal to 1. For example, the evaluation of [log<sub>3</sub> 27] is 3, because ((27/3)/3)/3 = 1. 

## Linear Function

`O(n)`

This function arises in algorithm analysis any time we have to do a single basic operation for each of `n` elements.

## N-Log-N Function
`O(n log n)`

It is the function that assigns to an input `n` the value of n times the logarithm base-two of `n`. This function grows a little more rapidly than the linear function and a lot less rapidly than the quadratic function.

## Quadratic Function

**O(n<sup>2</sup>)**

The main reason why the quadratic function appears in the analysis of algorithms is that there are many algorithms that have nested loops, where the inner loop performs a linear number of operations and the outer loop is performed a linear number of times.

## Cubic Function

**O(n<sup>3</sup>)**

This function appears less frequently in the context of algorithm analysis than the constant, linear, and quadratic functions previously mentioned, but it does appear from time to time.

## Exponential Function

**O(b<sup>n</sup>)**

As was the case with the logarithm function, the most common base for the exponential function in algorithm analysis is `b = 2`. 

For example, an integer word containing `n` bits can represent all the nonnegative integers less than 2<sup>n</sup>. If we have a loop that starts by performing one operation and then doubles the number of operations performed with each iteration, then the number of operations performed in the n<sup>th</sup> iteration is 2<sup>n</sup>




**Data Structures and Algorithms in Python**
*Goodrich T. Michael, Tamassia Roberto & Goldwasser H. Michael*
John Wiley & Sons,Inc (2013)
