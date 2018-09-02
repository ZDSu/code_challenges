// https://www.hackerrank.com/challenges/js10-function/problem


function factorial(n) {
    let fact = 1;
    for (let i = n; i > 0; i--) {
        fact *= i;
    }
    return fact
}


function factorial(n) {
    if (n > 1) {
        return n * factorial(n - 1);
    }
    
    return 1;
}


function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    
    return n * factorial(n - 1);
}