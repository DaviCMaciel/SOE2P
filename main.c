#include <stdio.h>
#ifdef _WIN64
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif


EXPORT float somaFloat(float num1, float num2) {
    return num1 + num2;
}