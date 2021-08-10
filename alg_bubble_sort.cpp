/******************************************************************************
# l0m1s
# lukes1582@gmail.com
algoritmo bubble sort sviluppato per C++
*******************************************************************************/
#include <iostream>
using namespace std;
int main(){

    int arrayA[5]={5,3,2,4,1};
    int lenArray = 5;
    cout << lenArray << "\n";
    for(int jVar=0;jVar<lenArray;jVar++){
        cout<<arrayA[jVar]<<" ";}
        cout<<endl;
        for(int iVar=0;iVar<(lenArray-1);iVar++){
            for(int kVar=0;kVar<(lenArray-1-iVar);kVar++){
                if(arrayA[kVar+1]<arrayA[kVar]){
                    int temp=arrayA[kVar+1];
                    arrayA[kVar+1]=arrayA[kVar];
                    arrayA[kVar]=temp;
                }
            }
            for(int wVar=0;wVar<lenArray;wVar++){
                cout<<arrayA[wVar]<<" ";
            }
        cout<<endl;
    }
}

