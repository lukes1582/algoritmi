/******************************************************************************
# l0m1s
# lukes1582@gmail.com
algoritmo insertion sort sviluppato per Java
*******************************************************************************/
public class alg_insertion_sort{
	public static void main(String[] args) {
	
		int arrayC[]={7,2,9,6,1,0,45};
        for(int aVar=0; aVar<arrayC.length;aVar++){
            System.out.print(Integer.toString(arrayC[aVar])+" ");
        }
        System.out.println();
        
        for(int bVar=1;bVar<arrayC.length;bVar++){
            int cVar=0;
            while(arrayC[cVar]<arrayC[bVar]){
                cVar++;
            }
            int temp=arrayC[bVar];

            for(int dVar=bVar-1;dVar>=cVar;dVar--){
                arrayC[dVar+1]=arrayC[dVar];
            }
            arrayC[cVar]=temp;
            
            for(int eVar=0;eVar<arrayC.length;eVar++){
                System.out.print(Integer.toString(arrayC[eVar])+" ");
            }
            System.out.println();	

	    }
    }
}
