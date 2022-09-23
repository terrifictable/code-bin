#include <iostream>
#include <string.h>
#include <stdio.h>


int main(int argc, char** argv) {
    if (argc < 2) { 
        std::cout << __FILE__ << " <hex-val without \"0x\">" << std::endl;
        return -1;
    }


    char* in = argv[1];
    std::cout << std::stoul(in, nullptr, 16) << " | " << in << std::endl;


    return 0;
}

