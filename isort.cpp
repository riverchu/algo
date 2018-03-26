#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

using namespace std;
const int N=10;

void isort(int a[]){
    for(int i=1; i<N; i++){
        int value = a[i], j;
        for(j=i;j>0 && a[j-1]>value; j--){//&&运算符的执行顺序为先左后右
                a[j]=a[j-1];
        }
        a[j] = value;
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
