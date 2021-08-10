/******************************************************************************
# l0m1s
# lukes1582@gmail.com
insertion sort sviluppato per C++
*******************************************************************************/

#include <iostream>
using namespace std;

int main(){
    int arrayC[5]={7,2,9,6,1};

    for(int aVar=0; aVar<5;aVar++){
        cout<<arrayC[aVar]<<" ";
    }
    cout<<endl;
    
    for(int bVar=1;bVar<5;bVar++){
        int cVar=0;
        while(arrayC[cVar]<arrayC[bVar]){
            cVar++;
        }
        int temp=arrayC[bVar];

        for(int dVar=bVar-1;dVar>=cVar;dVar--){
            arrayC[dVar+1]=arrayC[dVar];
        }
        arrayC[cVar]=temp;
        
        for(int eVar=0;eVar<5;eVar++){
            cout<<arrayC[eVar]<<" ";
        }
        cout<<endl;

    }
}

