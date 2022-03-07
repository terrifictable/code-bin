#include <stdlib.h>
#include <stdio.h>

void file_content(char *filename, char *method, FILE *fptr)
{
    fptr = fopen(filename, method);

    if (method == "r")
    {
        while (1)
        {
            char c = fgetc(fptr);
            if (c != EOF)
                printf("%c", c);
            else
                break;
        }
    }
    else if (method == "w")
    {
        char *content;

        printf("File Content: ");
        fgets(content, 1000000000, stdin);

        fprintf(fptr, "%s\n", content);
    }
    else if (method == "a")
    {
        char *content;

        prinf("File Content: ");
        fgets(content, 100000000, stdin);

        fputs(content, fptr);
    }
    else
    {
        printf("Invalid Method\n");
    }

    fclose(fptr);
}

int main(int argc, char *argv[])
{
    FILE *fptr;
    char *filename = "a.txt";
    char *method = "r";

    file_content(filename, method, fptr);
    getchar();
}
