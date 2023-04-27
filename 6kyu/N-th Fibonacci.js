/*
I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that, when given a number n (n >= 1 ), returns the nth number in the Fibonacci Sequence.

For example:

   nth_fib(4) == 2
Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
 */

// first solution
const nthFibo = (n) => {
    let t = 0;
    const arr = [0, 1];
    while (t !== n) {
        arr.push(arr[t] + arr[t + 1])
        t = t + 1;
    }
    return arr[t - 1]
};

// second solution
const nthFibo = (n) => {
    let a = 0, b = 1;
    for (let i = 0; i < n - 1; i++) {
        [a, b] = [b, a + b];
    }
    return a;
};