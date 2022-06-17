#include <stdio.h>


int char_to_dec(char input) {
    return (int) input;
}   
char dec_to_char(int input) {
    return (char) input;
}

// !no spaces in execution arguments!
// usage Windows:         ./whatever.exe someStringInput
// usege everythin else:  ./whatever someStringInput
int main(int argc, char *argv[]) {

    char *string = argv[1];
    int length = sprintf(string, "%s", string);

    for (int i=0; i < (length); i++) {
        printf("%c | %d\n", string[i], char_to_dec(string[i]));
    }

    return 0;
}
