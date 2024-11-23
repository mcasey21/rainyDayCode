/*
AUTHOR: michael casey
DATE: 08/03/24
PROGRAM: decimal to binary 
*/

#include <stdio.h>

#define SIZE 8

int main()
{

    int decimal_num;
    int binary_num[SIZE] = {};
    int one_to_twofivefive[SIZE] = {128, 64, 32, 16, 8, 4, 2, 1};
    int i;

    printf("Enter decimal number (0 to exit): ");  
    scanf("%d", &decimal_num);

    for (i = 0; i < SIZE; i++)
    {
        if(decimal_num >= one_to_twofivefive[i])
        {

            binary_num[i] = 1;                
            decimal_num -= one_to_twofivefive[i];

        }
        else
        {
            binary_num[i] = 0;
        }
    }

    for (i = 0; i < SIZE; i++)
    {
        printf("%d", binary_num[i]);
    }
  

    return 0;
}