#include <stdio.h>

int main() {
    int number1 , number2 ,sum;
    

    printf("Enter two Integers: ");
    scanf("%d %d", &number1, &number2);

    sum = number1 + number2;

    printf("Sum = %d", sum);

    return 0;
}