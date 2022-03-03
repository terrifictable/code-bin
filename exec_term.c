#include <stdlib.h>
#include <stdio.h>

void exec_cmd(char *command)
{
    FILE *fptr;
    char c;

    system(command);
    fptr = fopen("temp.txt", "r");

    while (1)
    {
        c = fgetc(fptr);
        if (c != EOF)
            printf("%c", c);
        else
            break;
    }
    fclose(fptr);
    remove("temp.txt");
}

int main(int argc, char *argv[])
{
    exec_cmd("echo Hi");
    // getchar();
}
