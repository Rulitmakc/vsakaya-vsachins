#include <iostream>
#include <clocale>
using namespace std;

int main(){
    
    setlocale(LC_ALL, "RU");
    srand(time(NULL));

int  rapnd = 1 + rand() % 20;
bool stop = false;
int user;
do {
    cout << "\033[31mугадай число\n";
    cout <<"\033[34mввведи число: ";
    cin >> user;
    if (rapnd != user)
    cout << "\033[31mне угадал\n";
    else
    stop = true;

} while (!stop);
cout << "\033[34mты угадал\n" << "\033[0m";
return 0;
}