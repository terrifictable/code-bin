using System;

namespace cs
{
    class Program
    {
        static void Main(string[] args) {
            string op = "";
            while ( true ) {
                op = GetOp();
                if (op == "exit") break;
                string res = Calculator(op);
                Console.WriteLine(res);
            }

            Console.ReadKey();
        }

        static string GetOp() {
            Console.Write("\nOperator >>> ");
            string op = Console.ReadLine();
            return op;
        }

        static string Calculator(string op) {
            if (op == "h") {
                return "---- HELP ----\n'h' > Help\n'+' > Add two nums together\n'-' > Subtract two nums\n'*' > Multiply two nums\n'/' > Subtract two nums\n'%' Modulus of two nums";
            }

            Console.Write("Enter two Numbers seperated by commas >>> ");
            string num = Console.ReadLine();
            double num1 = 0.0;
            double num2 = 0.0;

            try {
                string[] nums = num.Split(",");
                num1 = Convert.ToDouble(nums[0]);
                num2 = Convert.ToDouble(nums[1]);
            } catch {
                return "Invalid Input\nType 'h' for operators";
            }

            if (op == "+") {
                return (num1 + num2).ToString();
            } else if (op == "-") {
                return (num1 - num2).ToString();
            } else if (op == "*") {
                return (num1 * num2).ToString();
            } else if (op == "/") {
                return (num1 / num2).ToString();
            } else if (op == "%") {
                return (num1 % num2).ToString();
            } else if (op == "exit" || op == "x") {
                return "exit";
            } else {
                return "Invalid Operator\nType 'h' for all operators";
            }
        }
    }
}
