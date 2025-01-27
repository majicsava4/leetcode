#include <iostream>
using namespace std;
/*Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0*/
int main(){

    int x;
    int res;
    cin >> x;
    
    if(x < 9){
        res = x;
    }
    if(x % 9 == 0){
        res = 9;
    }else{
        res = x % 9;
    }
    
    
    cout << res;

    return 0;
}