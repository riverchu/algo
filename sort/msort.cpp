#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

using namespace std;
const int N = 100;

void merge(int a[], int left,int llen,int right,int rlen){
    int t[llen+rlen];
    int l=0,r=0,n=0;
    while (l< llen&&r< rlen){
        t[n++] = a[left+l]<a[right+r] ? a[left+l++] : a[right+r++];
    }

    while (l<llen) t[n++]=a[left+l++];
    while (r<rlen) t[n++]=a[right+r++];

    for(int i=0; i< llen+rlen; i++){
        a[left+i] = t[i];
    }

    return;
}

void msort(int a[],int left, int right){
    if(left>=right){
        return ;
    }

    int k = (left+right)/2;
    msort(a,left,k);
    msort(a,k+1,right);

    merge(a,left,k-left+1,k+1,right-k);
}

int main(){
    int a[N];
    srand(time(NULL));
    for(int i=0; i<N; i++){
        a[i] = rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    msort(a,0,N-1);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
