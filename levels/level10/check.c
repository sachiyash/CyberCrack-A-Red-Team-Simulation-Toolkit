#include <stdio.h>
#include <string.h>

int main() {
    char pass[20];
    printf("Enter password: ");
    scanf("%19s", pass);

    if(strcmp(pass, "cyber789") == 0) {
        printf("Correct! Flag: CyberCrack{Binary_Secrets}\n");
    } else {
        printf("Incorrect password!\n");
    }

    return 0;
}
