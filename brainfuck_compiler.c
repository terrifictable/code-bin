#include <stdio.h>
#include <stdlib.h>

#define DATASIZE 1001

void brainfuck(char *command_pointer, char *input) {
    int bracket_flag;
    char command;
    char data[DATASIZE] = {0};
    char *dp; 
    // dp = &data[DATASIZE / 2]; // idk?

    while (command = *command_pointer++)
        switch (command) {
        case '>':
            dp++;
            break;
        case '<':
            dp--;
            break;
        case '+':
            (*dp)++;
            break;
        case '-':
            (*dp)--;
            break;
        case '.':
            printf("%c", *dp);
            break;
        case ',':
            *dp = *input++;
            break;
        case '[':
            if (!*dp) {
                for (bracket_flag = 1; bracket_flag; command_pointer++)
                    if (*command_pointer == '[')
                        bracket_flag++;
                    else if (*command_pointer == ']')
                        bracket_flag--;
            }
            break;
        case ']':
            if (*dp) {
                command_pointer -= 2;
                for (bracket_flag = 1; bracket_flag; command_pointer--)
                    if (*command_pointer == ']')
                        bracket_flag++;
                    else if (*command_pointer == '[')
                        bracket_flag--;
                command_pointer++;
            }
            break;
        }
        
    printf("\n");
}


int main(int argc, char *argv[]) {
    char *buffer = 0;
    long length;
    FILE *fp;
    char *ch;

    fp = fopen (argv[1], "r");

    if (fp) {
        fseek(fp, 0, SEEK_END);
        length = ftell(fp);
        fseek(fp, 0, SEEK_SET);
        buffer = (char*) malloc((length + 1) * sizeof(char));
        
        if (buffer) {
            fread(buffer, sizeof(char), length, fp);
        }
        fclose(fp);
    }
    buffer[length] = '\0';


    brainfuck(buffer, "");
    return 0;
}
