import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class JavaGenerics {
    static < T > void printArray(T[] inputArray) {
        for (T elemToPrint : inputArray) {
            System.out.println(elemToPrint);
        }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> stringArray = new ArrayList<>();
        ArrayList<Integer> intArray = new ArrayList<>();

        while (scan.hasNext()) {
            try {
                int integerInput = scan.nextInt();
                intArray.add(integerInput);
            } catch (InputMismatchException e) {
                String stringInput = scan.next();
                stringArray.add(stringInput);
            }
        }
        printArray(intArray.toArray());
        printArray(stringArray.toArray());
    }
}
