#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char* pin = getenv("pin");
    char user_pin[20];

    printf("Enter the pin: ");
    scanf("%19s", user_pin);  // Limit input to prevent buffer overflow

    if (pin != NULL && strcmp(pin, user_pin) == 0)
    {
        printf("Welcome User!");
    }
    else
    {
        printf("Access Denied!");
    }

    return 0;
}


