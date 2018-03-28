#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>

using namespace std;
const int N = 10;
const int MAX = 100;

void csort(int a[]){
    int t[MAX] = {0};
    for(int i=0; i<N; i++){
        t[a[i]]++;
    }

    for(int i=0,j=0; i<MAX;i++){
        while(t[i]-->0)
            a[j++]=i;
    }
}

int main(){
    int a[N];
    srand(time(NULL));
    for(int i=0; i<N; i++){
        a[i] = rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    csort(a);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
