/*
AUTHOR: michael casey
DATE: 27/11/23
PROGRAM: calculating fibonacci sequence to the user entered term
*/

#include <stdio.h>

int main()
{
    int fibonacci[20] = {0,1}; // initialise index 0 and 1
    int i = 0;
    int no_terms = 0;
    int choice = 0;

    printf("Welcome to the Fibonacci series program\n\n");
    printf("Enter your selection: \n");

    printf("1. Enter the number of terms to calculate in the sequence and display\n2. End program\n");
    scanf("%d", &choice); // choice for program

    while(choice == 1) // executes program while choice picked is 1
    {
        printf("enter the number of terms to be calculated (max 20)\n"); // get term number
        scanf("%d", &no_terms);

        if(no_terms>0 && no_terms<21) // only allows numbers 1-20
        {
            for(i = 2; i < no_terms; i++ ) // loop to add index
            {
                fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]; // i starts at 2 so have to minus 2 and 1
            }// end loop

            printf("\nthe sequence to the %dth term is: \n", no_terms);
            for(i = 0; i < no_terms; i++ ) // loop to print sequence
            {
                printf("%d, ", fibonacci[i]);
            }// end loop

            printf("\n\n1. Enter the number of terms to calculate in the sequence and display\n2. End program\n");
            scanf("%d", &choice);
        }// end if

    }// end while

    if(choice==2) // ends program
    {
        printf("Goodbye!");
    }

    return 0;
}