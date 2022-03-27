#include <iostream>
#include <time.h>
using namespace std;

// HOW TO COMPILE:
// g++ -o $OUPUTFILE_NAME $THIS_FILE_NAME

string gen()
{
    srand(rand());
    string pass;

    string data = "abcdefghijklmnopqrstuvwxyz"
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  "0987654321"
                  "~`!@#$%^&*()-=_+[]|{};:,./<>";

    for (int i = 1; i <= 12; i++)
    {
        pass = pass + data[rand() % 93];
    }
    return pass;
}

int main()
{
    string pswd;
    int amount;

    cout << "Amount of passwords to generated\n>";
    cin >> amount;

    for (int i = 0; i < amount; i++)
    {
        pswd = gen();
        cout << pswd << "\n";
    }

    return 0;
}
