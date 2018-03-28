#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

#define len(x) sizeof(x)/sizeof(x[0])

using namespace std;
const int N = 10;

int* merge(int left[],int llen,int right[],int rlen){
    int l=0,r=0,n=0;
    int t[llen+rlen];
    while (l<llen&&r<rlen){
        t[n++] = left[l]<right[r] ? left[l++] : right[r++];
    }

    while (l<llen) t[n++]=left[l++];
    while (r<rlen) t[n++]=right[r++];

    return t;
}

int*  msort(int a[],int left, int right){
    if(left>=right){
        return NULL;
    }

    int k = (left+right)/2;
    int l[k-left],r[right-k-1];
    &l = msort(a,left,k);
    &r = msort(a,k+1,right);

    return merge(l,len(l),r,len(r));
}

int main(){
    int a[N];
    srand(time(NULL));
    for(int i=0; i<N; i++){
        a[i] = rand()%100;
        cout << setw(3) << a[i];
    }
    cout << endl;

    *a = msort(a,0,N-1);

    for(int i=0; i<N; i++){
        cout << setw(3) << a[i];
    }
    cout << endl;

    return 0;
}
