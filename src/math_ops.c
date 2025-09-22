#include "math_ops.h"

int complex_calc(int a, int b) {
    // Calls add from main.c and compute from utils.c
    int sum = add(a, b);
    int comp = compute(sum);
    return multiply(comp, 3);  // Also calls multiply from main.c
}