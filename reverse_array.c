#include <stdio.h>

#define N 5

int main() 
{ 
    int array[N], i;

    printf("Enter %d integer numbers\n", N);
    for(i=0; i<N; i++)
    {
        scanf("%d", &array[i]);
    }

    printf("Elements of array are: \n");
    for(i=N-1; i >= 0; i--)
    {
        printf("%d\n", array[i]);
    }

    return 0;
}