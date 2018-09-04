// https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem


function fibonacci(n) {
    if (n > 2) {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    else if (n < 1) {
        return 0;
    }
    return 1;
}