#include <iostream>

using namespace std;

char getOp()
{
    char op;
    cout << "Enter operator (h = help): " << endl;
    cout << "[>] $ "; cin>>op; cout << endl;
    return op;
}

int getNum()
{
    int num1, num2;

    cout << "Enter first Number: " << endl;
    cout << "[>] $ "; cin>>num1; cout << endl;

    cout << "Enter secont Number: " << endl;
    cout << "[>] $ "; cin>>num2; cout << endl;

    return num1, num2;
}

int main()
{
    int result, num1, num2;
    char op;

    op = getOp();
    if(op == 'h') {
        cout << "'h' = help          " << endl;
        cout << "'+' = Addition      " << endl;
        cout << "'-' = Subtraction   " << endl;
        cout << "'*' = Multiplication" << endl;
        cout << "'/' = Division      " << endl << endl;
        getOp();
    } else if(op == '+' || op == '-' || op == '*' || op == '/') {
        num1, num2 = getNum();

        if(op == '+') {
            result = num1+num2;
        } else if(op == '-') {
            result = num1-num2;
        } else if(op == '/') {
            result = num1/num2;
        } else if(op == '*') {
            result = num1*num2;
        } else {
            result = -1;
        }

        if(result != -1) {
            cout << endl << "Result: " << result;
        }
    } else {
            cout << "[ERROR] Invalid Input ('"<<op<<"')";
            getOp;
        }
    return 0;
}
