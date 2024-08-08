#include<iostream>
using namespace std;
int main(){
    int arr[] = {10,20,30};
    cout << *arr << endl;
    cout << arr << endl;
    //cout << arr++ << endl; gives error array beahves similar to pointer but cant perfor arithmetic operations
    int *ptr =  arr ;

    for (int i = 0 ; i< (sizeof(arr)/sizeof(arr[1])) ; i++){
        cout << *ptr << endl;
        cout << ptr << endl;
        ptr++;
    }

    //int *xptr = &arr; //cant initialize this statement

    //new git comment
    
    


}