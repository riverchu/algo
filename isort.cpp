#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

using namespace std;
const int N=10;

void isort(int a[]){
    for(int i=1; i<N; i++){
        for(int j=i; j>0; j--){
            int k = j-1;
            if(a[j]<a[k]){
                a[j]^=a[k];
                a[k]^=a[j];
                a[j]^=a[k];
            }
        }
    }
    return ;
}

int main(){
    int a[N];
    srand(time(NULL));
    for(int i=0; i<N; i++){
        a[i]=rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    isort(a);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
