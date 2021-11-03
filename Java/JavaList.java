import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class JavaList {
    static Scanner scan = new Scanner(System.in);

    public static List<Integer> createList() {
        List<Integer> myList = new ArrayList<>();
        int numOfElements = scan.nextInt();
        while (numOfElements-- > 0) {
            myList.add(scan.nextInt());
        }
        return myList;
    }

    public static void main(String[] args) {
        List<Integer> myList = createList();

        int numOfQueries = scan.nextInt();
        while (numOfQueries-- > 0) {
            String operationToPerform = scan.next();
            int indexToPerformOperationOn = scan.nextInt();

            if (operationToPerform.equals("Insert")) {
                int newNumber = scan.nextInt();
                myList.add(indexToPerformOperationOn, newNumber);
            } else {
                myList.remove(indexToPerformOperationOn);
            }
        }
        scan.close();
        for(int element : myList) {
            System.out.format("%s ", element);
        }
    }
}