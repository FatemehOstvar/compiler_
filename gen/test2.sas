#include <iostream>
#define PI 3.14159

class Circle {
    double radius;

    double area() {
        return PI * radius * radius;
    }
};

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 10;
    float y = 20.5;
    bool flag;

    if (x < y) {
        x = x + 1;
    } elsif (x == y) {
        x = x * 2;
    } else {
        x = x - 1;
    }

    for (int i = 0; i < 5; i = i + 1) {
        y = y + i;
    }

    while (x > 0) {
        x = x - 1;
    }

    int result = add(x, y);
    return result;
}
