#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 10;

void adjust(int a[], int len, int index){
    int left = 2*index + 1;
    int right = 2*index + 2;
    int maxIdx = index;
    if(left<len && a[left] > a[maxIdx]) maxIdx = left;
    if(right<len && a[right] > a[maxIdx])maxIdx = right;
    if(maxIdx != index){
        swap(a[maxIdx],a[index]);
        adjust(a, len, maxIdx);
    }
}

void hsort(int a[], int size){
    for(int i=size/2 - 1; i>=0; i--){
        adjust(a,size,i);
    }

    for(int i=size-1; i>0; i--){
        swap(a[0],a[i]);
        adjust(a,i,0);
    }
}


int main(){
    int a[N];
    srand(time(NULL));
    for(int i=0; i<N; i++){
        a[i]=rand()%100;
        cout << setw(3) <<a[i];
    }
    cout << endl;

    hsort(a,N);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
