#include <stdio.h>
int main() {
    int intType;
    float floatType;
    double doubleType;
    char charType;

    printf("Size of in: %1d bytes\n", sizeof(intType));
    printf("Size of float: %ld bytes\n", sizeof(floatType));
    printf("Size of double: %ld bytes\n", sizeof(doubleType));
    printf("Size of char: %ld byte\n", sizeof(charType));
    
    return 0;
}