/*
PROGRAM: 
AUTHOR: Michael Casey
DATE: 17/04/2024
*/

#include <stdio.h>
#include <string.h>

// SYMBOLIC NAMES
#define SIZE 100

// STRUCTURES

// FUNCTION SIGNATURES

int main()
{
    char sentence1[SIZE];
    char sentence2[SIZE];


    FILE *file1 = fopen("file1.txt", "r");
    FILE *file2 = fopen("file2.txt", "r");


    if (file1 == NULL || file2 == NULL)
    {
        printf("Error opening files for reading\n");
        return 0;
    }

    fgets(sentence1, SIZE, file1);
    fgets(sentence2, SIZE, file2);

    fclose(file1);
    fclose(file2);

    if (strcmp(sentence1, sentence2) == 0) 
    {
        printf("The files file1.txt and file2.txt are the same.\n");
    } 
    else 
    {
        printf("The files file1.txt and file2.txt are different.\n");
        
        printf("file1.txt LINE 1: %s\n", sentence1);
        printf("file2.txt LINE 2: %s\n", sentence2);
    }

    return 0;
}
