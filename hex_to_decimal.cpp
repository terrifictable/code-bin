#include <iostream>
#include <cstring>
#include <cmath>


int main() {
    char hex_num[100];
    int decimal_num = 0;
    int total = 0;

    std::cout << "Enter a hexadecimal number: ";
    std::cin >> hex_num;
    std::cout << std::endl;
    if (strlen(hex_num) > 2 && strncmp(hex_num, "0x", 2) == 0) {
        strcpy(hex_num, hex_num + 2);
    }

    std::cout << "Hexadecimal number: " << hex_num << std::endl;
    std::cout << "Decimal number: ";
    for (int i = 0; i < strlen(hex_num); i++) {
        decimal_num = 0;
        switch (hex_num[i]) {
            case '0':
                decimal_num += 0 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '1':
                decimal_num += 1 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '2':
                decimal_num += 2 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '3':
                decimal_num += 3 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '4':
                decimal_num += 4 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '5':
                decimal_num += 5 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '6':
                decimal_num += 6 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '7':
                decimal_num += 7 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '8':
                decimal_num += 8 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case '9':
                decimal_num += 9 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case 'a':
                decimal_num += 10 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case 'b':
                decimal_num += 11 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case 'c':
                decimal_num += 12 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case 'd':
                decimal_num += 13 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case 'e':
                decimal_num += 14 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            case 'f':
                decimal_num += 15 * pow(16, strlen(hex_num) - i - 1);
                total += decimal_num;
                break;
            default:
                std::cout << "Invalid input" << std::endl;
                return 0;
        }
        std::cout << decimal_num << ", ";
    }
    std::cout << std::endl;
    std::cout << "Total: " << total << std::endl;

    return 0;
}
