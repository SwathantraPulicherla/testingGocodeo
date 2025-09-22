#include "math_ops.h"

int complex_calc(int a, int b) {
    // Calls add from main.c and compute from utils.c
    int sum = add(a, b);
    int comp = compute(sum);
    return multiply(comp, 2);  // Also calls multiply from main.c
}

int simple_math(int x, int y) {
    // Calls add and multiply from main.c
    int result = add(x, y);
    return multiply(result, 3);
}

int advance_calc(int val) {
    // Calls compute from utils.c and multiply from main.c
    int comp = compute(val);
    return multiply(comp, 4);
}