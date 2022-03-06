#include <stdlib.h>
#include <stdio.h>

void exec_cmd(char *command)
{
    system(command);
}

void exec_js(char *code)
{
    FILE *fptr;
    fptr = fopen("./temp.js", "w");

    fprintf(fptr, "%s\n", code);
    fclose(fptr);

    system("node ./temp.js");
    remove("temp.js");
}

void exec_c(char *code)
{
    // this is completely useless
    FILE *fptr;
    fptr = fopen("./temp.c", "w");

    fprintf(fptr, "%s\n", code);
    fclose(fptr);

    system("gcc ./temp.c -o temp");
    remove("temp.c");
    system("temp.exe");
    remove("temp.exe");
}

void exec_py(char *code)
{
    FILE *fptr;
    fptr = fopen("./temp.py", "w");

    fprintf(fptr, "%s\n", code);
    fclose(fptr);

    system("python3 temp.py");
    remove("temp.py");
}

int main(int argc, char *argv[])
{
    exec_cmd("echo Hello World!");
    exec_js("console.log(\"Hello World!\")");
    exec_c("#include <stdio.h>\nint main() { printf(\"Hello World!\"); return 0; }");
    exec_py("print(\"Hello World!\")");
}
