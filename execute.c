#include <stdlib.h>
#include <stdio.h>

void exec_cmd(char *command)
{
    system(command); // run terminal command
}

void exec_js(char *code)
{
    FILE *fptr = fopen("./temp.js", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write code
    fclose(fptr);                // close temp file

    system("node ./temp.js"); // execute temp file
    remove("temp.js");        // remove temp file
}

void exec_c(char *code)
{
    FILE *fptr = fopen("./temp.c", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write code
    fclose(fptr);                // close temp file

    system("gcc ./temp.c -o temp"); // compile temp file
    remove("temp.c");               // remove temp file
    system("temp.exe");             // execute compiled code
    remove("temp.exe");             // remove compiled code file
}

void exec_cpp(char *code)
{
    FILE *fptr = fopen("./temp.cpp", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write code
    fclose(fptr);                // close temp file

    system("gcc ./temp.cpp -o temp"); // compile temp file
    remove("temp.cpp");               // remove temp file
    system("temp.exe");               // execute temp executable
    remove("temp.exe");               // remove temp executable
}

void exec_java(char *code)
{
    FILE *fp = fopen("./temp.java", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("java ./temp.java"); // execute temp file
    remove("temp.java");        // remove temp file
}

void exec_kotlin(char *code)
{
    FILE *fp = fopen("./temp.kt", "w"); // create an open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("kotlinc temp.kt -include-runtime -d ./temp.jar"); // compile temp file  (takes some time)
    remove("temp.kt");                                        // remove temp file
    system("java -jar ./temp.jar");                           // execute compiled temp file
    remove("temp.jar");                                       // remove compiled temp file
}

void exec_py(char *code)
{
    FILE *fptr = fopen("./temp.py", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write temp file
    fclose(fptr);                // close temp file

    system("python3 temp.py"); // execute temp file
    remove("temp.py");         // remove temp file
}

int main(int argc, char *argv[])
{
    exec_cmd("echo Hello World! { Teminal }");                                                                                            // Execute stuff from/in terminal
    exec_js("console.log(\"Hello World! { Node.js }\")");                                                                                 // Execute Node.js code
    exec_c("#include <stdio.h>\nint main() { printf(\"Hello World! { C }\\n\"); }");                                                      // Execute C code (why would you ever want to use this?)
    exec_cpp("#include <stdio.h>\nint main() { printf(\"Hello World! { C++ }\\n\"); }");                                                  // Execute C++ Code
    exec_java("public class temp {\n public static void main(String[] args) {\n System.out.println(\"Hello World! { Java }\"); \n} \n}"); // Execute Java Code
    exec_kotlin("fun main() {\n println(\"Hello World! { Kotlin }\"); \n}");                                                              // Execute Kotlin Code (this will take some time)
    exec_py("print(\"Hello World! { Python }\")");                                                                                        // Execute Python Code
}
