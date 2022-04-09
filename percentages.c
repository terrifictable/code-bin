#include <stdio.h>


int percentage(g, pw) { return (g / pw) * 100; }
int percentage_val(g, p) { return g * p / 100; }
int val_calc(p, pw) { return (pw * 100) / p; }


int main()
{
    int base = 600;
    int percentage = 30;
    int fraction = 180;

    printf("%d\n", percentage(base, fraction));
    printf("%d\n", percentage_val(base, percentage));
    printf("%d\n", val_calc(percentage, fraction));
}
