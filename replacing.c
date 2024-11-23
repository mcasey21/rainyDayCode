#include <stdio.h>

#define SIZE 10

int main()
{
    int i = 0;
    char barack[SIZE] = {'y','e','s',' ','w','e',' ','c','a','n'};

    printf("BEFORE: ");

    for(i=0;i<SIZE;i++)
    {
        printf("%c", barack[i]);
    }

    for(i=0;i<SIZE;i++)
    {
        if(barack[i] == ' ')
        {
            barack[i] = '_';
        }
    }

    printf("\nAFTER: ");

    for(i=0;i<SIZE;i++)
    {
        printf("%c", barack[i]);
    }

    return 0;
}