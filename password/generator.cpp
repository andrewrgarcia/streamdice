// forked from codespeedy's random-password (https://www.codespeedy.com/generate-a-random-password-of-a-specific-length-in-cpp/)
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
const char alphanum[] = "0123456789!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
int string_length = sizeof(alphanum) - 1;
int main()
{
    int n;
    cout << "Enter the length of password:";
    cin >> n;
    srand(time(0));
    cout << "Generated password:\n";
    for (int i = 0; i < n; i++)
        cout << alphanum[rand() % string_length];
    cout << endl;
    return 0;
}