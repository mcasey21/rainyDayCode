#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    int user_enter;
    int verify;
    char user_password[20];
    char password[] =  "secret123";

    printf("Press 1 to reveal secret: \n");

    if (scanf("%d", &user_enter) != 1 || sizeof(user_enter) != sizeof(int))
    {
        printf("Invalid input ..... shutting\n");
        return 0;
    }

    do
    {
        printf("Press 1 to reveal secret: \n");
        scanf("%d", &user_enter);

    } while (user_enter != 1);
    

    if (user_enter == 1)
    {
        printf("Enter password: \n");
        scanf("%s", user_password);
        
        verify = strcmp(password, user_password);

        if (verify == 0)
        {
            printf("This is the secret!!\n");
        }
        else
        {
            printf("Access Denied!\n");
        }
    }

    return 0;
}
