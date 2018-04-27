#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;
const int N=10;

void qsort(int a[],int left,int right){
    if(left>=right)
        return;

    int l = left;
    int r = right;
    int key = a[left];

    while(l<r){
        while(l<r && key<=a[r])r--;
        a[l]=a[r];
        while(l<r && a[l]<=key)l++;
        a[r]=a[l];
    }
    a[l] = key;

    qsort(a,left,l-1);
    qsort(a,l+1,right);

    return;
}

int main(){
    int a[N];
    srand(time(NULL));

    for(int i=0; i<N; i++){
        a[i]=rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    qsort(a,0,N-1);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
