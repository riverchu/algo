#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

using namespace std;
const int N=10;

void shellsort(int a[],int len){
    if(len<=1)
        return;
    for(int div=len/2; div>0; div/=2){
        for(int i=0; i<div; i++){
            for(int j=div; j<N; j+=div){
                for(int k=j; k>0; k-=div){
                    int m = k-div;
                    if(a[m]>a[k]){
                        a[m]^=a[k];
                        a[k]^=a[m];
                        a[m]^=a[k];
                    }
                }
            }
        }
    }

    return;
}

int main(){
    int a[N];
    srand(time(NULL));

    for(int i=0; i<N; i++){
        a[i] = rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    shellsort(a,N);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
