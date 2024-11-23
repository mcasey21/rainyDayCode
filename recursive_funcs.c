

#include <stdio.h>

int factorial(int);
int power(int, int);
int fib(int);
int sumdigits(int);

int main()
{
    //!recursive factorial function
    int num = printf("enter a number for factorial: ");
    scanf("%d", &num);
    int result_fact = factorial(num);
    printf("%d! = %d",num, result_fact);

    //!recursive power function
    int base = printf("\n\nenter a base: ");
    scanf("%d", &base);
    int expo = printf("enter a exponent: ");
    scanf("%d", &expo);
    int result_power = power(base, expo);
    printf("%d^%d = %d",base, expo, result_power);

    //!recursive power function
    int term = printf("\n\nenter a term for fibonnaci: ");
    scanf("%d", &term);
    int result_fib = fib(term);
    printf("fibonnci seq for %d terms = %d", term, result_fib);

    //!recursive sumdigits function
    int digit = printf("\n\nenter a digit: ");
    scanf("%d", &digit);
    int result_sumdigit = sumdigits(digit);
    printf("sum of %d = %d", digit, result_sumdigit);

    return 0;
}

//recursive factorial function
int factorial(int n)
{
    if (n == 1 || n ==0)
        return 1;
    else
        return n * factorial(n-1);
}

//recursive power function
int power(int x, int y)
{
    if (y == 0)
        return 1;
    else
        return x * power(x, y-1);

}

//recursive fibonnaci function
int fib(int t) 
{
    if (t <= 1) 
        return t;
    else
        return fib(t - 1) + fib(t - 2);
}

//recursive sumdigit function
int sumdigits(int d)
{
    if (d < 10) 
        return d;
    else
        return d % 10 + sumdigits(d / 10);
    
}