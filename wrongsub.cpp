#include <iostream>
using namespace std;
int main(){
    int number;
    cin >> number;
    int k;
    cin >> k;
    int x = 0;
    while(x<k){
        if (number%10== 0){
            number = number/10;
            x++;
            
        }
        else{
            number = number-1;
            x++;
        }
        
    }
    cout << number ;

}