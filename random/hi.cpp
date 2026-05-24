#include <bits\stdc++.h>
using namespace std;

void printName(string name, int count){
    if(count == 0) return;
    cout << name << endl;
    printName(name, count-1);
}
int main()
{
    printName("soumil", 3);
    return 0;
}
