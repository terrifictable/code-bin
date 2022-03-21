#include <stdlib.h>
#include <stdio.h>

void exec_cmd(char command[])
{
    system(command); // run terminal command
}

void exec_js(char code[])
{
    FILE *fptr = fopen("./temp.js", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write code
    fclose(fptr);                // close temp file

    system("node ./temp.js"); // execute temp file
    remove("temp.js");        // remove temp file
}

void exec_c(char code[])
{
    FILE *fptr = fopen("./temp.c", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write code
    fclose(fptr);                // close temp file

    system("gcc ./temp.c -o temp.exe"); // compile temp file
    remove("temp.c");                   // remove temp file
    // system("chmod +x temp.exe");      // make the file executable
    system("temp.exe"); // execute compiled code
    remove("temp.exe"); // remove compiled code file
}

void exec_cpp(char code[])
{
    FILE *fptr = fopen("./temp.cpp", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write code
    fclose(fptr);                // close temp file

    system("gcc ./temp.cpp -o temp.exe"); // compile temp file
    remove("temp.cpp");                   // remove temp file
    // system("chmod +x temp.exe");      // make the file executable
    system("temp.exe"); // execute temp executable
    remove("temp.exe"); // remove temp executable
}

void exec_java(char code[])
{
    FILE *fp = fopen("./temp.java", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("java ./temp.java"); // execute temp file
    remove("temp.java");        // remove temp file
}

void exec_kotlin(char code[])
{
    FILE *fp = fopen("./temp.kt", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("kotlinc temp.kt -include-runtime -d ./temp.jar"); // compile temp file  (takes some time)
    remove("temp.kt");                                        // remove temp file
    system("java -jar ./temp.jar");                           // execute compiled temp file
    remove("temp.jar");                                       // remove compiled temp file
}

void exec_perl(char code[])
{
    FILE *fp = fopen("./temp.perl", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("perl temp.perl"); // execute temp file
    remove("temp.perl");      // remove temp file
}

void exec_ruby(char code[])
{
    FILE *fp = fopen("./temp.ruby", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("ruby temp.ruby"); // execute temp file
    remove("temp.ruby");      // remove temp file
}

void exec_lua(char code[])
{
    FILE *fp = fopen("./temp.lua", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write code
    fclose(fp);                // close temp file

    system("lua temp.lua"); // execute temp file
    remove("temp.lua");     // remove temp file
}

void exec_py(char code[])
{
    FILE *fptr = fopen("./temp.py", "w"); // create and open temp file

    fprintf(fptr, "%s\n", code); // write temp file
    fclose(fptr);                // close temp file

    system("python3 temp.py"); // execute temp file
    remove("temp.py");         // remove temp file
}

void exec_go(char code[])
{
    FILE *fp = fopen("./temp.go", "w"); // create and open temp file

    fprintf(fp, "%s\n", code); // write temp file
    fclose(fp);                // close temp file

    system("go build temp.go"); // compile temp file
    remove("temp.go");          // remove temp file
    system("./temp");           // execute compiled file
    remove("temp");             // remove compiled file
}

int main(int argc, char *argv[])
{
    char code_cmd[] = "echo Hello World! { Teminal }";
    char code_c[] = "#include <stdio.h>\nint main() { printf(\"Hello World! { C }\\n\"); }";
    char code_go[] = "package main \nimport \"fmt\" \nfunc main() { fmt.Println(\"Hello World! { Go }\") }";
    char code_py[] = "print(\"Hello World! { Python }\")";
    char code_js[] = "console.log(\"Hello World! { Node.js }\")";
    char code_lua[] = "print(\"Hello World! { Lua }\")";
    char code_cpp[] = "#include <stdio.h>\nint main() { printf(\"Hello World! { C++ }\\n\"); }";
    char code_perl[] = "print \"Hello World! { Perl }\n\";";
    char code_ruby[] = "puts \"Hello World! { Ruby }\"";
    char code_java[] = "public class temp {\n public static void main(String[] args) {\n System.out.println(\"Hello World! { Java }\"); \n} \n}";
    char code_kotlin[] = "fun main() {\n println(\"Hello World! { Kotlin }\"); \n}";

    exec_c(code_c);           // Execute C code (why would you ever want to use this?)
    exec_go(code_go);         // Execute Go(Lang) code
    exec_js(code_js);         // Execute Node.js code
    exec_py(code_py);         // Execute Python Code
    exec_cmd(code_cmd);       // Execute stuff from/in terminal
    exec_lua(code_lua);       // Execute Lua Code
    exec_cpp(code_cpp);       // Execute C++ Code
    exec_perl(code_perl);     // Execute Perl Code
    exec_java(code_java);     // Execute Java Code
    exec_ruby(code_ruby);     // Execute Ruby Code
    exec_kotlin(code_kotlin); // Execute Kotlin Code
}
