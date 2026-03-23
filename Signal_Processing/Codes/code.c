#include <stdio.h>
#include <math.h>

typedef struct {
    double real;
    double imag;
} Complex;

int main() {
    // Numerator: s - 5 = 0
    // Zero: s = 5
    double zero = 5.0;

    // Denominator: (s + 2)(s + 3) = s^2 + 5s + 6 = 0
    // Using Quadratic Formula: s = [-b +/- sqrt(b^2 - 4ac)] / 2a
    double a = 1.0, b = 5.0, c = 6.0;
    double discriminant = b*b - 4*a*c;
    
    double pole1 = (-b + sqrt(discriminant)) / (2*a);
    double pole2 = (-b - sqrt(discriminant)) / (2*a);

    printf("--- System Analysis ---\n");
    printf("Zero: s = %.1f\n", zero);
    printf("Pole 1: s = %.1f\n", pole1);
    printf("Pole 2: s = %.1f\n", pole2);
    printf("-----------------------\n");

    // Logic to determine system properties
    if (pole1 > 0 || pole2 > 0) {
        printf("Result: System is UNSTABLE (Poles in RHP).\n");
    } else {
        printf("Result: System is STABLE (Poles in LHP).\n");
    }

    if (zero > 0) {
        printf("Result: System is NON-MINIMUM PHASE (Zero in RHP).\n");
    } else {
        printf("Result: System is MINIMUM PHASE.\n");
    }

    return 0;
}