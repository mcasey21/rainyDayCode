#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *ptr;
    int no_of_letters = 0;
    int vowel_counter = 0;


    printf("enter how many letters you need: ");
    scanf("%d", &no_of_letters);

    ptr = calloc(no_of_letters, sizeof(char));

    if(ptr == NULL)
    {
        printf("failed to allocate memory");
        return 0;
    }
    else
    {
        printf("memory allocation succesful\nenter your letters:\n");
        for(int i = 0; i < no_of_letters; i++)
        {
            scanf(" %c", ptr + i);
        }

        for(int i = 0; i < no_of_letters; i++)
        {
            switch(*(ptr + i))
            {
                case 'a':
                    vowel_counter++;
                    break;
                case 'e':
                    vowel_counter++;
                    break;
                case 'i':
                    vowel_counter++;
                    break;
                case 'o':
                    vowel_counter++;
                    break;
                case 'u':
                    vowel_counter++;
                    break;
                
            }
        }

        printf("your set of letters contained %d vowels", vowel_counter);
    }

    free(ptr);

    return 0;
}

