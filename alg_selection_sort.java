/******************************************************************************
# l0m1s
# lukes1582@gmail.com
algoritmo selection sort sviluppato per Java
*******************************************************************************/
public class alg_selection_sort {
	public static void main(String[] args) {
        int arrayB[]={5,9,2,3,1,0,4};

    for(int iVar = 0; iVar<arrayB.length; iVar++){
        System.out.print(Integer.toString(arrayB[iVar])+" ");
    }
    System.out.println();

    for(int jVar=0; jVar<arrayB.length-1;jVar++){ // dove 6 e' il valore della lunghezza dell'array meno 1
        int indexMin= jVar;

        for(int kVar= jVar+1;kVar<arrayB.length;kVar++){ // dove 7 è la lunghezza dell'array
            if(arrayB[indexMin]>arrayB[kVar]){
                indexMin=kVar;
            }
        }
        int temp=arrayB[jVar];
        arrayB[jVar]=arrayB[indexMin];
        arrayB[indexMin]=temp;
        
        for(int wVar=0;wVar<7;wVar++){
            System.out.print(Integer.toString(arrayB[wVar])+" ");
        }
        System.out.println();
	
    }
		

	}

}
