/*
AUTHOR: michael casey
DATE: 10/04/24
PROGRAM: hangman
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char word[7] = "coding";
    char user_guess[2];
    char word_layout[14] = "_ _ _ _ _ _ ";
    int guesses = 0;
    int correct_guess = 0;

    printf("--------HANGMAN 7 GUESSES-------");

    while(guesses < 7)
    {
        
        printf("\nGuess Letter -> ");
        fgets(user_guess, 2, stdin);

        if(strstr(word, &user_guess[0]) != NULL)
        {
            printf("\nletter in word\n");

            switch(user_guess[0])
            {
                case 'c':
                    word_layout[0] = 'c';
                    break;
                case 'o':
                    word_layout[2] = 'o';
                    break;
                case 'd':
                    word_layout[4] = 'd';
                    break;
                case 'i':
                    word_layout[6] = 'i';
                    break;
                case 'n':
                    word_layout[8] = 'n';
                    break;
                case 'g':
                    word_layout[10] = 'g';
                    break;
            }
        }
        else
        {
            printf("\nletter not in word\n");
        }

        for (int i = 0; i < 14; i++)
        {
            printf("%c", word_layout[i]);
            i++;
        }

        guesses++;

        while (getchar() != '\n');
    }

    printf("\nRan out of guesses");
    
    return 0;
}
