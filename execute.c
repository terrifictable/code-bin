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
    FILE *fptr;
    fptr = fopen("./temp.c", "w");

    fprintf(fptr, "%s\n", code);
    fclose(fptr);

    system("gcc ./temp.c -o temp");
    remove("temp.c");
    system("temp.exe");
    remove("temp.exe");
}

void exec_cpp(char *code)
{
    FILE *fptr;
    fptr = fopen("./temp.cpp", "w");

    fprintf(fptr, "%s\n", code);
    fclose(fptr);

    system("gcc ./temp.cpp -o temp");
    remove("temp.cpp");
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
    exec_cmd("echo Hello World! { teminal }");
    exec_js("console.log(\"Hello World! { Node.js }\")");
    exec_c("#include <stdio.h>\nint main() { printf(\"Hello World! { C }\"); return 0; }");
    exec_cpp("#include <stdio.h>\nint main() { printf(\"Hello World! { C++ }\"); }");
    exec_py("print(\"Hello World! { Python }\")");
}
