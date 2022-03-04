#include <stdlib.h>
#include <stdio.h>

void file_content(char *filename, char *method, FILE *fptr)
{
    fptr = fopen(filename, method);

    while (1)
    {
        char c = fgetc(fptr);
        if (c != EOF)
            printf("%c", c);
        else
            break;
    }

    fclose(fptr);
}

int main(int argc, char *argv[])
{
    FILE *fptr;
    char *filename = "a.txt";
    char *method = "r";

    file_content(filename, method, fptr);

    // getchar();
}
