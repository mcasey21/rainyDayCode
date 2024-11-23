/*
AUTHOR: michael casey
DATE:
PROGRAM: x = sum of f*x
         n = sum of f
*/

#include <stdio.h>

#define SIZE 6

int main()
{

    int x[SIZE];
    int f[SIZE];
    int fx[SIZE];
    int i;
    int n = 0;
    float total = 0;
    int sum_of_fx = 0;

    printf("\nEnter x's: \n");
    for(i = 0; i < SIZE; i++)
    {
        scanf("%d", &x[i]);
    }

    printf("\nEnter f's: \n");
    for(i = 0; i < SIZE; i++)
    {
        scanf("%d", &f[i]);
        n = n + f[i];
    }

    for(i = 0; i < SIZE; i++)
    {
        fx[i] = f[i] * x[i];
        sum_of_fx = sum_of_fx + fx[i];
    }


    total = (float)sum_of_fx/n;

    printf("%d/%d =  %.2f",sum_of_fx, n, total);
    

    return 0;
}