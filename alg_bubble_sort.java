/******************************************************************************
# l0m1s
# lukes1582@gmail.com
algoritmo bubble sort sviluppato per Java
*******************************************************************************/
public class alg_bubble_sort{

	public static void main(String[] args) {
		
		int arrayA[] = {9,5,3,4,0,2,1};
		int lenArray = arrayA.length;
		for(int aVar=0;aVar<lenArray;aVar++){
			System.out.print(Integer.toString(arrayA[aVar])+" ");
		}
		System.out.println();
		System.out.println("la lunghezza dell'array e' " + Integer.toString(lenArray));
		System.out.println();
		for(int jVar=0;jVar<lenArray;jVar++){
			for(int iVar=0;iVar<(lenArray-1);iVar++){
				for(int kVar=0;kVar<(lenArray-1-iVar);kVar++){
					if(arrayA[kVar+1]<arrayA[kVar]){
						int temp=arrayA[kVar+1];
						arrayA[kVar+1]=arrayA[kVar];
						arrayA[kVar]=temp;
					}
				}
				
			}
		}
		for(int wVar=0;wVar<lenArray;wVar++){
			System.out.print(Integer.toString(arrayA[wVar])+" ");
		}
		

		
	}
}
