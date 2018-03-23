#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>

using namespace std;
const int N = 10;

void bsort(int a[]){
    for(int i=0; i<N; i++){
        for (int j = 1; j<N-i; j++){
            int k = j-1;
            if(a[k]>a[j]){
                a[k]^=a[j];
                a[j]^=a[k];
                a[k]^=a[j];
            }
        }
    }
    return;
}

int main(){
    int a[N];
    srand(time(NULL));
    for (int i=0; i<N; i++){
        a[i]=rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    bsort(a);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
