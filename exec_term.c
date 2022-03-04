#include <stdlib.h>
#include <stdio.h>

void exec_cmd(char *command)
{
    system(command);
}

int main(int argc, char *argv[])
{
    exec_cmd("echo Hi");
    // getchar();
}
