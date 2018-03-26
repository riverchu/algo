#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;
const int N=10;

void qsort(int a[],int left,int right){
    if(left>=right)
        return;

    int i = left;
    int j = right;
    int key = a[left];

    while(i<j){
        while(i<j && key<=a[j])j--;
        a[i]=a[j];
        while(i<j && a[i]<=key)i++;
        a[j]=a[i];
    }
    a[i] = key;

    qsort(a,left,i-1);
    qsort(a,i+1,right);

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
