#include <clocale>
#include <iostream>

int main() {
    
    setlocale(LC_ALL, "RU");
    
    float n;
    float n1;
    int d;
    std::cout << "\033[31mчто делать:(1.-,2.+,3.*,4./) ";
    std::cin >> d;

    std::cout << "цифра: ";
    std::cin >> n;

    std::cout << "вторая цифра: \033[37m";
    std::cin >> n1;

    if (d == 1) {
    float r = n - n1;
    std::cout << r << " вычетание\n";
    }
    else if (d == 2) {
    float b = n + n1;
    std::cout << b << " сложение\n ";
    }
    else if (d == 3) {
    float y = n * n1;
    std::cout << y << " умножение\n ";
    }
    else if (d == 4) {
    float u = n / n1;
    std::cout << u << " деление\n";
    }
}
