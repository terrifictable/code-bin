#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <thread>

static const char alphabet[] = "0123456789" "!@#$%^&*" "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "abcdefghijklmnopqrstuvwxyz";
int strLen = sizeof(alphabet) - 1;

std::string generate(int n) {
    static std::string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    std::string result;
    result.resize(20);

    srand(time(NULL));
    for (int i = 0; i < 20; i++)
        result[i] = charset[(rand() * (n + 1)) % charset.length()];

    return result;
}


void create_new_file(int i) {
    FILE *fp;

    std::string rand_name = generate(i);

    std::string file_name;
    file_name.append("./");
    file_name.append(rand_name);
    file_name.append(".txt");
    
    fp = fopen(file_name.c_str(), "w");
    fprintf(fp, "%s\n", "Follow me: https://github.com/TerrificTable");
    fclose(fp);
}
 
int main() {
    int length = rand() * 1000;
    printf("%d Threads\n", length);
    
    std::thread threads[length + 1];

    for (int i=0; i < length; i++) {
        threads[i] = std::thread(create_new_file, i);
    }

    for (int i=0; i < length; i++) {
        threads[i].join();
    }

    printf("Finished!");

    return 0;
}
