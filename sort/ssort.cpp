#include <iostream>
#include <time.h>
#include <iomanip>
#include <cstdlib>

using namespace std;
const int N=10;

void Ssort(int a[]){
    for(int i=0; i<N-1; i++){
        int temp = i;
        for(int j=i+1; j<N; j++){
            if(a[temp]>a[j])temp = j;
        }
        if(temp!=i){
            int t = a[temp];
            a[temp] = a[i];
            a[i] = t;
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

    Ssort(a);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
