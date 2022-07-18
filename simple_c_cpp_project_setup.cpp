#include <iostream>
#include <cstring>
#include <cstdio>


#define COMPILER "c++11"
#define LANGUAGE "cpp" // "c" or "cpp"


char *readFile( const char *filename );
void writeFile( const char *filename, const char *filecontent );
void mkdir( const char *dirname );
char *replace( const char *input, const char *search, const char *replace );

int main() {
    std::cout << "\n [ Start ] \n" << std::endl;

    char *cFile = R"(
#include <stdio.h>

int main( int argc, char **argv ) {
    printf("\n [ Start ] \n");

    printf("Hello World!\n");

    printf("\n [ End ] \n");
    return 0;
}
    )";
    char *cppFile = R"(
#include <iostream>
#include <cstdio>

int main( int argc, char **argv ) {
    std::cout << "\n [ Start ] \n" << std::endl;

    std::cout << "Hello World!" << std::endl;

    std::cout << "\n [ End ] \n" << std::endl;
    return 0;
}
    )";

    mkdir( "include" );
    mkdir( "src" );

    if (LANGUAGE == "c") writeFile( "src/main.c", cFile );
    else writeFile( "src/main.cpp", cppFile );

    mkdir( "lib" );
    mkdir( "out" );

    std::cout << "\n [ End ] " << std::endl;
}


char *replace( const char *input, const char *search, const char *replace ) {
    char *output = new char[strlen( input ) + 1];
    int i = 0;
    int j = 0;
    while ( input[i] != '\0' ) {
        if ( strncmp( &input[i], search, strlen( search ) ) == 0 ) {
            strncpy( &output[j], replace, strlen( replace ) );
            j += strlen( replace );
            i += strlen( search );
        } else {
            output[j] = input[i];
            i++;
            j++;
        }
    }
    output[j] = '\0';
    return output;
}

void mkdir( const char *dirname ) {
    char command[256];
    sprintf( command, "mkdir %s", dirname );
    system( command );
}

void writeFile( const char *filename, const char *filecontent ) {
    FILE *fp = fopen( filename, "w" );
    fwrite( filecontent, 1, strlen( filecontent ), fp );
    fclose( fp );
}

char *readFile( const char *filename ) {
    FILE *fp = fopen( filename, "r" );

    fseek( fp, 0, SEEK_END );
    long size = ftell( fp );
    fseek( fp, 0, SEEK_SET );
    char *buffer = new char[size + 1];

    fread( buffer, 1, size, fp );
    buffer[size] = '\0';
    fclose( fp );
    return buffer;
}
