/******************************************************************************
# l0m1s
# lukes1582@gmail.com
algoritmo selction sort sviluppato per C++
*******************************************************************************/
#include <iostream>
using namespace std;

int main(){
    int arrayB[7]={5,4,2,3,1,0,9};

    for(int iVar = 0; iVar<7; iVar++){
        cout<<arrayB[iVar]<<" ";
    }
    cout<<endl;

    for(int jVar=0; jVar<6;jVar++){ // dove 6 e' il valore della lunghezza dell'array meno 1
        int indexMin= jVar;

        for(int kVar= jVar+1;kVar<7;kVar++){ // dove 7 è la lunghezza dell'array
            if(arrayB[indexMin]>arrayB[kVar]){
                indexMin=kVar;
            }
        }
        int temp=arrayB[jVar];
        arrayB[jVar]=arrayB[indexMin];
        arrayB[indexMin]=temp;
        
        for(int wVar=0;wVar<7;wVar++){
            cout<<arrayB[wVar]<<" ";
        }
        cout<<endl;
    }
}

