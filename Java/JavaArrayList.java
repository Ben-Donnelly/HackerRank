import java.util.ArrayList;
import java.util.Scanner;

public class JavaArrayList {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<int[]> arrayListOfArrays = new ArrayList<>();

        int numOfArrayLists = scan.nextInt();

        for(int i=0; i<numOfArrayLists; i++) {
            int numOfElementsInArray = scan.nextInt();
            int [] runningArray = new int[numOfElementsInArray];
            for(int j=0; j<numOfElementsInArray; j++) {
                runningArray[j] = scan.nextInt();
            }
            arrayListOfArrays.add(runningArray);
        }

        int numOfQueries = scan.nextInt();
        while (numOfQueries > 0) {
            int arrayNumberToQuery = scan.nextInt();
            int positionOfArrayToQuery = scan.nextInt();

            // It seems Hackerrank forgot that we count from 0
            int [] runningArrayList = arrayListOfArrays.get(arrayNumberToQuery - 1);
            try {
                System.out.println(runningArrayList[positionOfArrayToQuery - 1]);
            }
            catch (IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
            }
            numOfQueries--;
        }
    }
}
